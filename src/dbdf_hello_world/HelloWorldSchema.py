from pyspark.sql.types import *

HelloWorldSchema = StructType([
    StructField("coffeeBatchId", IntegerType()),
    StructField("smell", StringType()),
    StructField("weight", StringType()),
    StructField("date", DateType()),
    StructField("published", TimestampType()),
    StructField("color", StringType())
])