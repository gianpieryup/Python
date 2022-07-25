import pandas as pd
import numpy as np
# Si dejamos el scrip en la misma carpeta que los csv's solo debemos poner los nombres y no la ruta
name_oracle='oracle.csv'
name_hive='hive.csv'
header_nup_oracle = 'NUP'
header_nup_hive = 'cod_per_nup'


archivo_oracle=pd.read_csv(name_oracle)
archivo_hive=pd.read_csv(name_hive)

# Las cabeceras, para solo quedarnos con los nups
nup_oracle=archivo_oracle[header_nup_oracle]
nup_hive=archivo_hive[header_nup_hive]


print('-'*10,"HIVE",'-'*10)
archivo_hive["en_oracle"]=nup_hive.isin(nup_oracle)
print(archivo_hive.groupby(["en_oracle"]).count()[header_nup_hive],'\n')
en_hive_pero_no_en_oracle = np.setdiff1d(nup_hive, nup_oracle)
print("Algunos NUPS \n",en_hive_pero_no_en_oracle[:25],'\n')



print('-'*10,"ORACLE",'-'*10)
archivo_oracle["en_hive"]=nup_oracle.isin(nup_hive)
print(archivo_oracle.groupby(["en_hive"]).count()[header_nup_oracle],'\n')
en_oracle_pero_no_en_hive = np.setdiff1d(nup_oracle, nup_hive)
print("Algunos NUPS \n",en_oracle_pero_no_en_hive[:25])



'''
AUTOR: Gianpier Yupanqui
LAST MODIFICATION: 29/04/2022

NOTES
No hace falta quitar los 0 de la izquierda al leerlos con pandas ya se los quita

#crea y guarda en un archivo .csv con los resultados
archivo_hive.to_csv(r"add_columns.csv") 
'''





-- codigo a mejorar
#from abc import ABCMeta,abstractmethod
from abc import ABC, abstractmethod
import argparse
from logging import exception
import pyspark
import sys
import pyspark.sql.functions as psf
import json
from pyspark.sql import SparkSession
import re
import os
from pyspark.sql.types import StructType

class ValidationStrategy(ABC):

    #__metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    def _format_number(self, number):
        return format(number,',d')

    @abstractmethod
    def validate(self):
        pass

class RowCheckValidation(ValidationStrategy):

    def __init__(self, spark):

        self.spark = spark
        self.message = '\t-Status: {status}\n\t-Cloudera count: {cloudera_count}\n\t-AWS count: {aws_count}\n\t-Difference: {diff}\n'
        self.status = 'ERROR'

    def validate(self, data):

        cloudera_count, aws_count = data.get('df_cloudera').count(), data.get('df_aws').count()
        if cloudera_count == aws_count:
            self.status = 'SUCCESS'

        return self.message.format(
            status=self.status,
            cloudera_count=self._format_number(cloudera_count),
            aws_count=self._format_number(aws_count),
            diff = self._format_number(abs(cloudera_count - aws_count))
        )
        
class ColumnsCheckValidation(ValidationStrategy):

    def __init__(self, spark):

        self.spark = spark
        self.message = '\t-Status: {status}\n\t-Cloudera count: {cloudera_count}\n\t-AWS count: {aws_count}\n'
        self.status = 'ERROR'

    def validate(self, data):

        num_cols_cloudera = len(data.get('df_cloudera').columns)
        num_cols_aws = len(data.get('df_aws').columns)

        if num_cols_cloudera == num_cols_aws:
            self.status = 'SUCCESS'

        return self.message.format(
            status = self.status,
            cloudera_count = num_cols_cloudera,
            aws_count = num_cols_aws
        )

class NullsCheckValidation(ValidationStrategy):

    def __init__(self, spark):

        self.spark = spark
        self.status = 'SUCCESS'
        self.message='\t- Status: {status}\n\t- Nulls count:\n{nulls_count}'

    def validate(self, data):

        result = []
        df_aws = data.get('df_aws')
        fields_list = data.get('nulls_check')

        if fields_list:
            #Get nulls count
            for field in fields_list:
                null_number = df_aws.filter(df_aws[field].isNull()).count()
                result.append((field, null_number))

            for res in result:
                if res[1] != 0:
                    self.status = 'ERROR'
        else:
            self.status = 'OMITTED'

        return self.message.format(
            status=self.status,
            nulls_count = ''.join('\t\t- {}: {}\n'.format(x[0], self._format_number(x[1])) for x in result)
        )
        
class DiffCheckValidation(ValidationStrategy):

    def __init__(self, spark):
        
        self.spark = spark
        self.message = '\n\t-Status: {status}\n\t-Diff Count: {diff_count}\n\t-Diff Cloudera:\n{diff_cloudera}\n\t-Diff aws:\n{diff_aws}\n'
        self.message2 = '\n\t-Status: {status}\n\t-Grain: {grain}\n\tColumns with differences: {cols}\n\t'
        self.status = 'ERROR'

    def getShowString(self, df, n=20, truncate=False, vertical=False):

        if df is None:
            return None
        if isinstance(truncate, bool) and truncate:
            return(df._jdf.showString(n, 20, vertical))
        else:
            return(df._jdf.showString(n, int(truncate), vertical))

    def get_diff(self, df1, df2, grain):

        columns_with_differences = []
        diff1,diff2 = None, None

        if not grain:
            diff1 = df1.exceptAll(df2)
            diff2 = df2.exceptAll(df1)
            return diff1, diff2

        for col in df1.columns:
            if col in grain:
                continue

            evaluate_cols = grain + col.split(',') # Generate list with grain and specific column

            #Get partial dataframes
            df1_partial = df1.select(*evaluate_cols)
            df2_partial = df2.select(*evaluate_cols)

            #Get difference from partial dataframes
            diff1_partial = df1_partial.exceptAll(df2_partial)
            #Get difference from partial dataframes
            diff2_partial = df2_partial.exceptAll(df1_partial)

            #Si la differencia entre los data frames parciales es mayor a cero, guardo esa columna porque tiene diferencias
            if diff1_partial.count() > 0 and diff2_partial.count() > 0:
                columns_with_differences.append(col)

        if columns_with_differences:
            for g in reversed(grain):
                columns_with_differences.insert(0, g)
            diff1 = df1.exceptAll(df2).select(*columns_with_differences).orderBy(*grain)
            diff2 = df2.exceptAll(df1).select(*columns_with_differences).orderBy(*grain)
        return diff1, diff2

    def get_diff_by_col(self, df1, df2, grain):

        columns_with_differences = []
        diff1,diff2 = None, None
        #Returns list of columns where a difference was found
        if not df1 or not df2 or not grain:
            raise Exception('diff_by_col recieved wrong arguments')

        res = {}
        columns_with_differences = []

        for col in df1.columns:
            if col in grain: #Ignorar por ahora
                continue

            evaluate_cols = grain + col.split(',') # Generate list with grain and specific column

            #Get partial dataframes
            df1_partial = df1.select(*evaluate_cols)
            df2_partial = df2.select(*evaluate_cols)

            #Get difference from partial dataframes
            diff1_partial = df1_partial.exceptAll(df2_partial).orderBy(*grain)
            diff2_partial = df2_partial.exceptAll(df1_partial).orderBy(*grain)

            #Si la differencia entre los data frames parciales es mayor a cero, guardo esa columna porque tiene diferencias
            if diff1_partial.count() > 0 and diff2_partial.count() > 0:
                res.update({
                        col: (diff1_partial,diff2_partial)
                    })
                columns_with_differences.append(col)
        return res, columns_with_differences

    def validate(self, data):

        #Get dataframes from input
        df_cloudera = data.get('df_cloudera')
        df_aws = data.get('df_aws')
        columns = df_cloudera.schema.names

        #Get settings and grain
        settings = data.get('settings')
        grain = data.get('grain')

        if settings.get('diff_by_col'):
            if not grain:
                raise Exception('Grain is empty and diff_by_col was requested')
            res, columns_with_differences = self.get_diff_by_col(df_cloudera, df_aws, grain)

            message = self.message2.format(status=self.status, grain=grain, cols = columns_with_differences) + '\n'

            for col, dfs in res.items():
                message = message + '\nColumn: {column}'.format(column = col) + '\nDiff Count: {diff_count}\n'.format(diff_count=dfs[0].count()) + '\nCloudera:\n'+  self.getShowString(dfs[0]) + '\n' + '\nAWS:\n' + self.getShowString(dfs[0]) 

            return message
        else:
            if not grain:
                diff_cloudera = df_cloudera.exceptAll(df_aws)
                diff_aws = df_aws.exceptAll(df_cloudera)

            diff_cloudera, diff_aws = self.get_diff(df_cloudera, df_aws, grain)

            try:
                diff_count = diff_cloudera.count()
            except:
                diff_count = 0


            if diff_count == 0:
                self.status = "SUCCESS"

            return self.message.format(
                status=self.status,
                diff_count = self._format_number(diff_count),
                diff_cloudera = self.getShowString(diff_cloudera, n = settings.get('df_show')),
                diff_aws = self.getShowString(diff_aws, n = settings.get('df_show'))
        )

#No implementado  
class NumPartitionsCheckValidation(ValidationStrategy):
    #tiene que revisar los directorios para las carpetas tanto en hdfs como s3
    def __init__(self, spark):
        self.spark = spark
    def validate(self,data):
        pass

#No implementado 
class DuplicatesCheckValidation(ValidationStrategy):
    def __init__(self, spark):
        self.spark = spark
    def validate(self,data):
        pass

#No implementado 
class DateCheckValidation(ValidationStrategy):
    def __init__(self, spark):
        self.spark = spark
    def validate(self,data):
        pass

class PartitionComparer:

    def __init__(self, input):

        self.INPUT_VARS = ['tables_to_check','grain','validations','partitions', 'nulls_check', 'settings']
        #Mapeo de validaciones
        self.VALIDATIONS = {
            'diff_check': DiffCheckValidation,
            'row_check':RowCheckValidation,
            'col_check':ColumnsCheckValidation,
            'num_partitions_check':NumPartitionsCheckValidation,
            'nulls_check': NullsCheckValidation
        }

        self.DEFAULT_SETTINGS = {
            'df_show': 50,
            'checkpoint':False,
            'cache':False,
            'diff_by_column':True,
            'order_by':''
        }

        #Spark initialization
        self.spark = self._get_contexts()
        self.spark.sparkContext.setCheckpointDir('/santander/bi-corp/tmp/checkpoints')

        #Get input
        self.input = self._parse_input(input)
        #self.input = self._get_input()

    def _get_contexts(self): # Ok

        spark = SparkSession.builder \
            .enableHiveSupport() \
            .config('spark.sql.parquet.binaryAsString', 'true') \
            .config('spark.cleaner.referenceTracking.cleanCheckpoints', 'true') \
            .config("mapred.input.dir.recursive","true") \
            .config("mapreduce.input.fileinputformat.input.dir.recursive","true") \
            .config("spark.sql.hive.convertMetastoreParquet", "false") \
            .getOrCreate()

        global log
        log = spark._jvm.org.apache.log4j.LogManager.getLogger('test')
        level = spark._jvm.org.apache.log4j.Level.INFO
        log.setLevel(level)

        return spark

    def _pretty_print_json(self, json_obj, sort=True, indents=4): #string o json

        if type(json_obj) is str:
            print(json.dumps(json.loads(json_obj), sort_keys=sort, indent=indents))
        else:
            print(json.dumps(json_obj, sort_keys=sort, indent=indents))
        return None

    def _cast_input(self, input):

        input = input.replace(' ', '')
        try:
            return int(input)
        except:
            try:
                if isinstance(eval(input.capitalize()), bool):
                    return eval(input.capitalize())
            except:
                return input.split(',')

    def _parse_input( self, raw_input):

        regex = '^([^\s\t\r\n]*)=([^\s\t\r\n]*)$'
        parsed_input = {}

        for key, val in raw_input.items():
            if len(val) == 0:
                continue
            if key in ('grains', 'nulls_check'):
                if len(raw_input['tables_to_check'].split(',')) == 1:
                    parsed_input[key] = {
                        raw_input['tables_to_check'].strip().split('.')[1] if len(raw_input['tables_to_check'].split('.'))>1 else raw_input['tables_to_check'].strip()  : val.replace(' ','').split(',')
                    }
                else:
                    parsed_input[key] = {
                        re.search(regex, v.replace(' ','')).group(1) : self._cast_input(re.search(regex, v).group(2))
                        for v in val.replace(' ','').split(';')
                    }
            if key == 'settings':
                parsed_input[key] = {
                        re.search(regex, v.replace(' ','')).group(1) : self._cast_input(re.search(regex, v).group(2))
                        for v in val.replace(' ','').split(';')
                    }
            if key in ('tables_to_check', 'partitions', 'validations'):
                parsed_input[key] = val.replace(' ','').split(',')

        return parsed_input

    def _get_input(self):
        
        #Get Input
        raw_input = {}
        for var in self.INPUT_VARS:
            #Get value from env variable
            val = os.getenv(var)
            #Store value
            if val is not None and len(val)>0:
                raw_input.update({var:val})

        #Excepciones
        if not raw_input['tables_to_check']:
            raise Exception('No tables where passed')

        return self._parse_input(raw_input)

    def _get_validator(self, validation):

        for key, obj in self.VALIDATIONS.items():
            if key == validation:
                return obj

    def _get_table_location(self, table_name):

        regex = '^hdfs:\/\/.*(\/santander\/?.*)(staging|common|business)(\/.*\/)([^\/]*)$'
        try:
            cloudera_location = self.spark.sql("describe formatted {table}".format(table=table_name)).filter("col_name=='Location'").collect()[0].data_type
            aws_location = re.sub(regex, "s3a://sarp1ae1as3zonda0lake001\\1\\2\\3\\4", cloudera_location)
        except Exception as e:
            raise Exception('Failed to read table location for {table}\n Exception:\n {e}\n'.format(table=table_name,e=e))

        return cloudera_location, aws_location

    def _get_partition_name(self, table_name):

        try:
            df = self.spark.sql("describe  {table}".format(table=table_name))
            partition_list = df.select(df.col_name, df.data_type).rdd.map(lambda x:(x[0],x[1])).collect()
            partition_details = [partition_list[index+1:] for index,item in enumerate(partition_list) if item[0]=='# col_name']
            partitions = [x for x in partition_details[0][0]]

            return partitions #lista con nombre de particiones
        except:
            return []

    def _get_environments_df(self, table, partition, checkpoint = False, cache = False):

        df_aws, df_cloudera = None, None
        cloudera_location, aws_location = self._get_table_location(table)
        partition_name = []
        try:
            partition_name = self._get_partition_name(table)[0]
        except:
            pass

        if checkpoint and cache: cache = not cache

        if partition is None: # Para tablas no particionadas

            cloudera_path = cloudera_location
            aws_path = aws_location

        elif len(partition.split("/")) > 1:#Para multiples particiones

            cloudera_path = os.path.join(cloudera_location, partition)
            aws_path = os.path.join(aws_location, partition)

        else:
            
            cloudera_path = os.path.join(cloudera_location, partition_name) + '=' + partition
            aws_path = os.path.join(aws_location, partition_name) + '=' + partition

        try:

            df_cloudera = self.spark.read.parquet(cloudera_path)
            df_aws = self.spark.read.parquet(aws_path)

        except:
            try:
                df_cloudera = self.spark.read.parquet(cloudera_path + "/*")
                df_aws = self.spark.read.parquet(aws_path + "/*")
            except:
                try:
                    df_cloudera = self.spark.read.parquet(cloudera_path)
                    df_aws = self.spark.read.parquet((lambda x: x.replace("/fact","").replace("/dim",""))(aws_path))
                except Exception as e:
                    raise e

        if checkpoint:
            df_cloudera.checkpoint()
            df_aws.checkpoint()
        if cache:
            df_cloudera.cache()
            df_aws.cache()

        return df_cloudera, df_aws

    def _validate(self, table, partition=None):

        table_name = table.split('.')[1] if len(table.split('.')) > 1 else table
        schema = 'bi_corp_common' if len(table.split('.')) == 1 else table.split('.')[0]
        grains = self.input.get('grains')
        try:
            grain = grains.get(table_name)
        except:
            grain = None
        nulls_check = self.input.get('nulls_check')
        null_check_cols = nulls_check.get(table_name) if nulls_check is not None else None

        try:
            settings = self.input.get('settings')
            df_cloudera, df_aws = self._get_environments_df(
                                                schema + '.' + table_name, 
                                                partition, 
                                                checkpoint = settings.get('checkpoint'),
                                                cache = settings.get('cache')
                                            )
        except Exception as e:
            print('Failed to read parquet for {table} at {partition_date} due to:\n{e}'.format(table=table, partition_date=partition,e=e))
            raise e

        results = {}
        for validation in self.input.get('validations'):

            if validation not in self.VALIDATIONS.keys():
                print("Validation {} provided doesnt exist\n".format(validation))
                continue

            data = {
                "table": table_name,
                "schema": schema,
                "grain" : grain,
                "partition":partition,
                "df_cloudera":df_cloudera,
                "df_aws":df_aws,
                "nulls_check": null_check_cols,
                "settings" : self.input.get('settings')
            }

            try:
                result = self._get_validator(validation)(self.spark).validate(data)
            except Exception as e:
                print('{validation} Failed to get results for {table} due to:\n{e}'.format(validation=validation,table=table_name,e=e))
                continue

            if validation not in results.keys():
                results[validation] = result


        for validation, result in results.items():
            print('{}\n{}'.format(validation.upper(), result))

    def execute(self):

        # Por cada tabla se muestra los resultados de cada particion para cada validacion
        for table in self.input['tables_to_check']:
            if self.input.get('partitions') is None:
                print('##################### Validation for {table} with no partitions ##################### '.format(table=table))
                try:
                    self._validate(table)
                except Exception as e:
                    raise e
            else:
                for partition in self.input['partitions']:
                    print('##################### Validation for {table} at partition_date = {partition} #####################'.format(table=table, partition=partition))
                    try:
                        self._validate(table, partition)
                    except Exception as e:
                        raise e
                    

if __name__ == '__main__':

    _input = {
        "tables_to_check":"bi_corp_staging.rio56_circuito",
        "grains":"", # Comma separated string of columns
        'validations':'col_check,row_check,diff_check',
        'partitions':'2022-07-21',
        'nulls_check':'',# Comma separated string of columns
        'settings':'df_show=50;checkpoint=true;cache=false;diff_by_col=false'
    }

    pc = PartitionComparer(_input)
    pc.execute()

