# coding=UTF-8
from os.path import expandvars
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, MapType
from pyspark.sql.functions import *


log = None
s = None
AWS_BUCKET_S3 = 'sarp1ae1as3zonda0lake001'


def get_contexts():
    spark = SparkSession.builder \
        .enableHiveSupport() \
        .appName("json_onboarding_unico - SPARK") \
        .config("spark.driver.maxResultSize", "0") \
        .config("spark.sql.crossJoin.enabled", "true") \
        .config("spark.sql.broadcastTimeout", "36000") \
        .config("spark.sql.autoBroadcastJoinThreshold", "-1") \
        .config("hive.exec.dynamic.partition.mode", "nonstrict") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.kryo.registrationRequired", "false") \
        .config("spark.shuffle.service.enabled","true") \
        .config("spark.dynamicAllocation.enabled=true") \
        .config("spark.dynamicAllocation.initialExecutors", "5") \
        .config("spark.dynamicAllocation.minExecutors", "4") \
        .config("spark.dynamicAllocation.maxExecutors", "12") \
        .config("spark.driver.memory", "10G") \
        .getOrCreate()

    global log
    log = spark._jvm.org.apache.log4j.LogManager.getLogger('mongo_evaluation')
    level = spark._jvm.org.apache.log4j.Level.INFO
    log.setLevel(level)    

    return spark


def andy_loader(spark):

    query_json = f"""
    select json, partition_date
    from bi_corp_staging.json_onboarding_unico
    where partition_date= '2023-09-13'
    """
    df_json = spark.sql(query_json)

    # Determine the schema of the JSON payload from the column(** chino)
    json_schema_df = spark.read.json(df_json.rdd.map(lambda row: row.json))
    json_schema = json_schema_df.schema

    # Apply the schema to payload to read the data    
    df_details = df_json.withColumn("parsed_data", from_json(df_json["json"], json_schema)).drop("json")
    # Bajamas un nivel para no hacer 'parsed_data.columna'
    df = df_details.select(col("parsed_data.*"),col("partition_date"))
    df.printSchema()



    print("EXPLOIDE delays")
    df = df.withColumn("delays_explode", explode_outer("delays"))

    print("EXPLOIDE evaluationAttempts")
    df = df.withColumn("evaluationAttempts_explode", explode_outer("evaluationAttempts"))

    print("EXPLOIDE internalErrors")
    df = df.withColumn("internalErrors_explode", explode_outer("internalErrors"))

    print("EXPLOIDE listOffer")
    df = df.withColumn("listOffer_explode", explode_outer("listOffer"))

    print("EXPLOIDE rejectionCause")
    df = df.withColumn("rejectionCause_explode", explode_outer("rejectionCause"))

    print("offerData: struct ")
    print("EXPLOIDE    |-- packages")
    df = df.withColumn("packages_explode", explode_outer("offerData.packages"))

    print("EXPLOIDE          |-- accounts")
    df = df.withColumn("accounts_explode", explode_outer("packages_explode.accounts"))

    print("EXPLOIDE          |-- cards")
    df = df.withColumn("cards_explode", explode_outer("packages_explode.cards"))

    print("EXPLOIDE                 |-- levels")
    df = df.withColumn("levels_explode", explode_outer("cards_explode.levels"))

    print("EXPLOIDE          |-- loans")
    df = df.withColumn("loans_explode", explode_outer("packages_explode.loans"))
    
   
    df_final= df.select(col("_id.$oid").alias("id"),
                    "obuId",
                    "flow",
                    "beginningFlow",
                    "endingFlow",
                    "hasDebitCard",
                    col("packages_explode._id").alias("packages_id"),
                    col("packages_explode.subProduct").alias("packages_sub_product"),
                    col("packages_explode.name").alias("packages_name"),
                    col("packages_explode.maxAssistance").alias("packages_maxAssistance"),
                    col("accounts_explode._id").alias("accounts_id"),
                    col("accounts_explode.name").alias("accounts_name"),
                    col("accounts_explode.currency").alias("accounts_currency"),
                    col("accounts_explode.overdraftLimits").alias("accounts_overdraftLimits"),
                    "delays_explode.name",
                    col("delays_explode.seconds").alias("del_seconds"),
                    #"delays_explode.date",
                    "delays_explode.date.$date",
                    "document_type",
                    "document_number",
                    "biometry_id",
                    "evaluationAttempts_explode.order",
                    "evaluationAttempts_explode.seconds",
                    col("partition_date")
                )
    
    df_final.printSchema()





    # QUITAR TODOS LOS SHOW PORQUE ESO DEMORA LA EJECUCION
    #   drop table if exists bi_corp_staging.onboarding_unico_spark;
    #   show CREATE TABLE bi_corp_staging.onboarding_unico_spark;

    df_final \
        .write \
        .partitionBy('partition_date') \
        .option("compression", 'gzip') \
        .saveAsTable(name='bi_corp_staging.onboarding_unico_spark',
                        format='parquet',
                        mode='Overwrite',
                        path='/santander/bi-corp/staging/onboarding/unico_spark')

if __name__ == "__main__":
    
    spark = get_contexts()
    
    # FIX1: "delays_explode.date", esto es un struct no podemos dejar un struct como campo final => "delays_explode.date.$date",
    # FIX2: col("hasDebitCard").cast(StringType()).alias("has_debit_card"),
    andy_loader(spark)   