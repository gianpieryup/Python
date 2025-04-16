# coding=UTF-8
from os.path import expandvars
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DoubleType, LongType
from pyspark.sql.functions import *

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

    return spark

def loader(spark):
    
    query_json = f"""
    select json, partition_date
    from table
    where partition_date= '2024-01-01'
    """
    
    df_json = spark.sql(query_json)

    # ======================================
    # Descargar un archivo de landing para ingerir la estructura por unica vez
    # 
    # df = spark.read.text("GIAN_20230920.csv")
    # json_schema_df = spark.read.json(df.rdd.map(lambda row: row.value))
    # json_schema = json_schema_df.schema
    # json_schema
    # # Copiar y pegar este resultado en la siguiente linea


    json_schema = StructType([
        StructField('_id', StructType([StructField('$oid', StringType(), True)]), True),
        StructField('delays', ArrayType(StructType([
            StructField('date', StructType([StructField('$date', LongType(), True)]), True), 
            StructField('name', StringType(), True), 
            StructField('seconds', LongType(), True)]), True), True), 
        StructField('offerData', StructType([
            StructField('offerId', StringType(), True), 
            StructField('packages', ArrayType(StructType([
                StructField('_id', StringType(), True), 
                StructField('accounts', StringType(), True)]), True), True), True]), True),
        StructField('status', StructType([
            StructField('code', StringType(), True), 
            StructField('date', StructType([StructField('$date', LongType(), True)]), True), 
            StructField('description', StringType(), True), StructField('detail', StringType(), True)]), True), 
        StructField('validationStatus', ArrayType(StructType([
            StructField('flow', StringType(), True), 
            StructField('passed', StringType(), True)]), True), True)
    ])


    #Apply the schema to payload to read the data 
    df = df_json.withColumn("parsed_data",from_json(col("json"),json_schema)) \
                   .select("parsed_data.*", col("partition_date"))



    # EXPLOID de una lista en VERTICAL
    print("EXPLOIDE delays")
    df = df.withColumn("delays_explode", explode_outer("delays"))

    # EXPLOID de una lista en HORIZONTAL
    df = df.select("*", 
        df.validationStatus[2].alias('f3'),
        df.offerData.packages[0].alias('of')
    )


    # SELECT FINAL
    df_final= df.select(col("_id.$oid").alias("id"),
        col("f3.flow").alias("flow3"),
        when(df.f3.passed != "false", None).otherwise(df.f3.status.code).alias("status_error_code3"),
        col("of._id").alias("ofd_pkg_id"),
        from_unixtime(col("status.date.$date")/1000, "yyyy-MM-dd HH:mm:ss").alias("status_date"),
        col("partition_date")
    )
    #df_final.show()
    df_final.printSchema()

    # print("EXAMPLE INDIVIDUAL")
    # df_final.filter("id = '6500fb91c8733d11d476d832'").show()


if __name__ == "__main__":
    spark = get_contexts()
    loader(spark)