from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, window, sum as spark_sum
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, TimestampType

schema = StructType([
    StructField("event_id", StringType()),
    StructField("customer_id", IntegerType()),
    StructField("amount", DoubleType()),
    StructField("event_type", StringType()),
    StructField("event_time", TimestampType()),
])

spark = SparkSession.builder.appName("TransactionStreaming").getOrCreate()
raw = (spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092")
       .option("subscribe", "transactions").option("startingOffsets", "earliest").load())

events = raw.select(from_json(col("value").cast("string"), schema).alias("e")).select("e.*")
events = events.dropDuplicates(["event_id"])

agg = (events.withWatermark("event_time", "2 minutes")
       .groupBy(window("event_time", "1 minute"))
       .agg(spark_sum("amount").alias("revenue")))

query = agg.writeStream.outputMode("update").format("console").option("truncate", False).start()
query.awaitTermination()
