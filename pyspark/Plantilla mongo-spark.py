# coding=UTF-8
from os.path import expandvars
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DoubleType, LongType
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
    log = spark._jvm.org.apache.log4j.LogManager.getLogger('mongo_unico')
    level = spark._jvm.org.apache.log4j.Level.INFO
    log.setLevel(level)    

    return spark

def riesgos_loader(spark):
    
    query_json = f"""
    select json, partition_date
    from bi_corp_staging.json_onboarding_unico
    where partition_date= '2023-10-31'  -- En produccion: '{expandvars('${partition_date}')}'
    """
    
    df_json = spark.sql(query_json)

    # ======================================
    # Descargar un archivo de landing para ingerir la estructura por unica vez
    # 
    # df = spark.read.text("ONBO_GIAN_20230920.csv")
    # json_schema_df = spark.read.json(df.rdd.map(lambda row: row.value))
    # json_schema = json_schema_df.schema
    # json_schema
    # # Copiar y pegar este resultado en la siguiente linea




    json_schema = StructType([StructField('_id', StructType([StructField('$oid', StringType(), True)]), True),
        StructField('admission',StructType([
                StructField('account_number',StringType(),True),
                StructField('admissionStatus',StringType(),True),
                StructField('asolSteep',StringType(),True),
                StructField('asol_errors',ArrayType(StructType([
                        StructField('code',StringType(),True),
                        StructField('description',StringType(),True),
                        StructField('message',StringType(),True)]),True),True),
                StructField('asol_number',StringType(),True),
                StructField('registration_date',StructType([StructField('$date',LongType(),True)]),True)
        ]),True),
        StructField('beginningFlow', StringType(), True), 
        StructField('biometry_id', StringType(), True),
        StructField('branch_office', StringType(), True),
        StructField('campaing', StringType(), True), 
        StructField('channel', StringType(), True), 
        StructField('collegeData', StructType([
                StructField('admissionDate', StringType(), True), 
                StructField('careerCode', StringType(), True), 
                StructField('universityCode', StringType(), True), 
                StructField('universityType', StringType(), True)]), True), 
        StructField('checklist_id', StringType(), True), 
        StructField('contact', StructType([
                StructField('call_me', StringType(), True), 
                StructField('email', StringType(), True), 
                StructField('is_valid_email', StringType(), True), 
                StructField('phone_area_code', StringType(), True), 
                StructField('phone_company', StringType(), True), 
                StructField('phone_number', StringType(), True)]), True), 
        StructField('createdDate', StructType([StructField('$date', LongType(), True)]), True), 
        StructField('delays', ArrayType(StructType([StructField('date', StructType([StructField('$date', LongType(), True)]), True), StructField('name', StringType(), True), StructField('responseStatus', LongType(), True), StructField('seconds', LongType(), True)]), True), True), StructField('document_number', StringType(), True), StructField('document_type', StringType(), True), StructField('dropoutFlowId', StringType(), True), 
        StructField('endingFlow', StringType(), True), 
        StructField('enriId', StringType(), True), 
        StructField('evaluationAttempts', ArrayType(StructType([StructField('order', LongType(), True), StructField('seconds', LongType(), True)]), True), True), 
        StructField('flow', StringType(), True), StructField('gclid', StringType(), True), 
        StructField('hasDebitCard', StringType(), True),
        StructField('inhabilitationCodes', StringType(), True), 
        StructField('internalErrors', ArrayType(StructType([
                StructField('date', StructType([StructField('$date', LongType(), True)]), True), 
                StructField('code', StringType(), True), 
                StructField('description', StringType(), True), 
                StructField('stacktrace', StringType(), True)
        ]), True), True),
        StructField('isClient', StringType(), True), 
        StructField('isHealthPersonel', StringType(), True),
        StructField('isInsurance', StringType(), True),
        StructField('isSorpresaSantander', StringType(), True),
        StructField('isWomen', StringType(), True),
        StructField('job', StructType([StructField('activity', StringType(), True), StructField('employee_quantity', LongType(), True), StructField('income', StringType(), True), StructField('ocupation_code', StringType(), True), StructField('tax_situation', StringType(), True), StructField('work_relationship_code', StringType(), True)]), True), StructField('listOffer', ArrayType(StructType([StructField('description', StringType(), True), StructField('name', StringType(), True), StructField('packageId', StringType(), True), StructField('price', DoubleType(), True), StructField('subproductId', StringType(), True)]), True), True), StructField('medium', StringType(), True), StructField('metadata', StructType([StructField('ip', StringType(), True), StructField('user_agent', StringType(), True)]), True), StructField('nup', StringType(), True), StructField('obuId', StringType(), True), StructField('offerData', StructType([StructField('offerId', StringType(), True), StructField('packages', ArrayType(StructType([StructField('_id', StringType(), True), StructField('accounts', ArrayType(StructType([StructField('_id', StringType(), True), StructField('currency', StringType(), True), StructField('name', StringType(), True), StructField('overdraftLimits', ArrayType(StringType(), True), True)]), True), True), StructField('cards', ArrayType(StructType([StructField('_id', StringType(), True), StructField('levels', ArrayType(StructType([StructField('_id', StringType(), True), StructField('limits', ArrayType(StringType(), True), True)]), True), True)]), True), True), StructField('loans', ArrayType(StructType([StructField('_id', StringType(), True), StructField('maxGrantable', StringType(), True), StructField('minGrantable', StringType(), True)]), True), True), StructField('maxAssistance', DoubleType(), True), StructField('name', StringType(), True), StructField('subProduct', StringType(), True)]), True), True)]), True), 
        StructField('ponsaId', StringType(), True),
        StructField('product', StructType([
                StructField('package_id', StringType(), True), 
                StructField('product_id', StringType(), True), 
                StructField('subproduct_id', StringType(), True)]), True), 
        StructField('prospect', StructType([StructField('address', StructType([StructField('complements', StringType(), True), StructField('department', StringType(), True), StructField('floor', StringType(), True), StructField('locality', StringType(), True), StructField('province', StringType(), True), StructField('street', StringType(), True), StructField('street_number', StringType(), True), StructField('zip_code', StringType(), True)]), True), 
            StructField('birth_date', StringType(), True), StructField('citizenship', StringType(), True), StructField('countryOfBirth', StringType(), True), StructField('cuil', StringType(), True), StructField('first_name', StringType(), True), StructField('gender', StringType(), True), StructField('last_name', StringType(), True), 
            StructField('nationality', StringType(), True), 
            StructField('pep', StringType(), True), 
            StructField('relationshipStatus', StringType(), True), 
            StructField('renaper_id', StringType(), True), 
            StructField('residenceCategory', StringType(), True),
            StructField('residenceExpirationDate',StructType([StructField('$date',LongType(),True)]),True)
        ]), True), 
        StructField('segment', StringType(), True), StructField('segmentObu', StringType(), True), 
        StructField('selectedCard', StringType(), True),
        StructField('source', StringType(), True), StructField('startAt', StringType(), True), StructField('status', StructType([StructField('code', StringType(), True), StructField('date', StructType([StructField('$date', LongType(), True)]), True), StructField('description', StringType(), True), StructField('detail', StringType(), True)]), True), StructField('track_id', StringType(), True), StructField('validationStatus', ArrayType(StructType([StructField('flow', StringType(), True), StructField('passed', StringType(), True), StructField('status', StructType([StructField('code', StringType(), True), StructField('date', StructType([StructField('$date', LongType(), True)]), True), StructField('description', StringType(), True), StructField('detail', StringType(), True)]), True)]), True), True)])


    #Apply the schema to payload to read the data    
    df_details = df_json.withColumn("parsed_data", from_json(df_json["json"], json_schema)).drop("json")
    #Bajamas un nivel para no hacer 'parsed_data.columna'
    df = df_details.select(col("parsed_data.*"),col("partition_date"))
    df.printSchema()



    # EXPLOID de una lista en VERTICAL
    print("EXPLOIDE delays")
    df = df.withColumn("delays_explode", explode_outer("delays"))

    # EXPLOID de una lista en HORIZONTAL
    df = df.select("*", 
        df.validationStatus[0].alias('f1'),  df.validationStatus[1].alias('f2'),  df.validationStatus[2].alias('f3'),
        df.listOffer[0].alias('lo1'),  df.listOffer[1].alias('lo2'),  df.listOffer[2].alias('lo3'),
        df.offerData.packages[0].alias('of')
    )


    # SELECT FINAL
    df_final= df.select(col("_id.$oid").alias("id"),
        col("admission.asol_errors").cast(StringType()).alias("admission_asol_errors"),
        from_unixtime(col("admission.registration_date.$date")/1000, "yyyy-MM-dd HH:mm:ss").alias("admission_registration_date"),
        col("admission.asol_number").alias("admission_asol_number"),
        col("admission.account_number").alias("admission_account_number"),
        col("admission.admissionStatus").alias("admission_admissionstatus"),
        col("admission.asolSteep").alias("admission_asolsteep"),
        "biometry_id",
        "branch_office",
        "campaing",
        "channel",
        "checklist_id",
        col("collegeData.admissionDate").alias("collegedata_admissiondate"),
        col("collegeData.careerCode").alias("collegedata_careercode"),
        col("collegeData.universityCode").alias("collegedata_universitycode"),
        col("collegeData.universityType").alias("collegedata_universitytype"),
        col("contact.call_me").alias("contact_call_me"),
        col("contact.email").alias("contact_email"),
        col("contact.phone_area_code").alias("contact_phone_area_code"),
        col("contact.phone_company").alias("contact_phone_company"),
        col("contact.phone_number").alias("contact_phone_number"),
        col("contact.is_valid_email").alias("contact_is_valid_email"), #-- este no estabaen el anterior
        from_unixtime(col("createdDate.$date")/1000, "yyyy-MM-dd HH:mm:ss").alias("createddate"),
        "document_number",
        "document_type",
        "enriid",
        col("endingFlow").alias("flow"),
        "hasdebitcard",
        "inhabilitationcodes",
        col("internalErrors.code").cast(StringType()).alias("internalerror_code"),
        col("internalErrors.date.$date").cast(StringType()).alias("internalerror_date"),
        col("internalErrors.description").cast(StringType()).alias("internalerror_description"),
        col("internalErrors.stacktrace").cast(StringType()).alias("internalerror_stacktrace"),
        col("isclient").cast(StringType()),
        col("ishealthpersonel").cast(StringType()),
        col("isinsurance").cast(StringType()),
        col("issorpresasantander").cast(StringType()),
        col("isWomen").cast(StringType()),
        col("job.activity").alias("job_activity"),
        col("job.employee_quantity").alias("job_employee_quantity"),
        col("job.income").alias("job_income"),
        col("job.ocupation_code").alias("job_ocupation_code"),
        col("job.tax_situation").alias("job_tax_situation"),
        col("job.work_relationship_code").alias("job_work_relationship_code"),
        "beginningFlow",
        "endingFlow",
        col("lo1.packageId").alias("listoffer_packageid1"),
        col("lo1.subproductId").alias("listoffer_subproductid1"),
        col("lo1.description").alias("listoffer_description1"),
        col("lo1.price").alias("listoffer_price1"),
        col("lo1.name").alias("listoffer_name1"),
        col("lo2.packageId").alias("listoffer_packageid2"),
        col("lo2.subproductId").alias("listoffer_subproductid2"),
        col("lo2.description").alias("listoffer_description2"),
        col("lo2.price").alias("listoffer_price2"),
        col("lo2.name").alias("listoffer_name2"),
        col("lo3.packageId").alias("listoffer_packageid3"),
        col("lo3.subproductId").alias("listoffer_subproductid3"),
        col("lo3.description").alias("listoffer_description3"),
        col("lo3.price").alias("listoffer_price3"),
        col("lo3.name").alias("listoffer_name3"),
        "medium",
        col("metadata.ip").alias("metadata_ip"),
        col("metadata.user_agent").alias("metadata_user_agent"),
        "nup",
        "obuId",
        "ponsaId",
        col("product.package_id").alias("product_package_id"),
        col("product.product_id").alias("product_product_id"),
        col("product.subproduct_id").alias("product_subproduct_id"),
        col("prospect.address.complements").alias("prospect_address_complements"),
        col("prospect.address.department").alias("prospect_address_department"),
        col("prospect.address.floor").alias("prospect_address_p_floor"),
        col("prospect.address.locality").alias("prospect_address_locality"),
        col("prospect.address.province").alias("prospect_address_province"),
        col("prospect.address.street").alias("prospect_address_street"),
        col("prospect.address.street_number").alias("prospect_address_street_number"),
        col("prospect.address.zip_code").alias("prospect_address_zip_code"),
        col("prospect.birth_date").alias("prospect_birth_date"),
        col("prospect.citizenship").alias("prospect_citizenship"),
        col("prospect.countryOfBirth").alias("prospect_countryofbirth"),
        col("prospect.cuil").alias("prospect_cuil"),
        col("prospect.first_name").alias("prospect_first_name"),
        col("prospect.gender").alias("prospect_gender"),
        col("prospect.last_name").alias("prospect_last_name"),
        col("prospect.nationality").alias("prospect_nationality"),
        col("prospect.pep").alias("prospect_pep"),
        col("prospect.relationshipStatus").alias("prospect_relationshipstatus"),
        col("prospect.renaper_id").alias("prospect_renaper_id"),
        col("prospect.residenceCategory").alias("product_residence_category"),
        col("prospect.residenceExpirationDate.$date").alias("product_residence_expirationdate"),
        col("f1.flow").alias("flow1"),
        col("f1.passed").alias("flow_passed1"),
        when(df.f1.passed != "false", None).otherwise(df.f1.status.code).alias("status_error_code1"),
        when(df.f1.passed != "false", None).otherwise(df.f1.status.description).alias("status_error_description1"),
        when(df.f1.passed != "false", None).otherwise(df.f1.status.detail).alias("status_error_detail1"),
        col("f2.flow").alias("flow2"),
        col("f2.passed").alias("flow_passed2"),
        when(df.f2.passed != "false", None).otherwise(df.f2.status.code).alias("status_error_code2"),
        when(df.f2.passed != "false", None).otherwise(df.f2.status.description).alias("status_error_description2"),
        when(df.f2.passed != "false", None).otherwise(df.f2.status.detail).alias("status_error_detail2"),
        col("f3.flow").alias("flow3"),
        col("f3.passed").alias("flow_passed3"),
        when(df.f3.passed != "false", None).otherwise(df.f3.status.code).alias("status_error_code3"),
        when(df.f3.passed != "false", None).otherwise(df.f3.status.description).alias("status_error_description3"),
        when(df.f3.passed != "false", None).otherwise(df.f3.status.detail).alias("status_error_detail3"),
        "selectedcard",
        "source",
        "startAt",
        col("status.code").alias("status_code"),
        from_unixtime(col("status.date.$date")/1000, "yyyy-MM-dd HH:mm:ss").alias("status_date"),
        col("status.description").alias("status_description"),
        col("status.detail").alias("status_detail"),
        "track_id",
        col("offerData.offerId").alias("offerdata_offerid"),
        col("of._id").alias("ofd_pkg_id"),
        col("of.subProduct").alias("ofd_pkg_subroduct"),
        col("of.name").alias("ofd_pkg_name"),
        col("of.maxAssistance").alias("ofd_pkg_maxAssistance"),
        col("of.accounts").cast(StringType()).alias("ofd_pkg_accounts_json"),
        col("of.cards").cast(StringType()).alias("ofd_pkg_cards_json"),
        col("of.loans").cast(StringType()).alias("ofd_pkg_loans_json"),
        
        col("partition_date")
    )
    #df_final.show()
    df_final.printSchema()

    # print("EXAMPLE INDIVIDUAL")
    # df_final.filter("id = '6500fb91c8733d11d476d832'").show()

    # .saveAsTable : Lo que hace es DROP/CREATE de la tabla
    # Te ayuda cuando esas desarrollando

    df_final \
        .write \
        .partitionBy('partition_date') \
        .option("compression", 'gzip') \
        .saveAsTable(name='bi_corp_staging.onboarding_unico_gian',
                        format='parquet',
                        mode='Overwrite',
                        path='/santander/bi-corp/staging/onboarding/unico_gian')
    
    # [ISSUE] Cuando ya tienes la estructura y vas a produccion, porfavor usar el metodo de guardado


if __name__ == "__main__":
    
    spark = get_contexts()
    
    riesgos_loader(spark)   