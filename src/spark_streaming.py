from pyspark.sql import SparkSession

SPARK_MASTER = "spark://spark:7077"


spark = (
    SparkSession.builder.appName("RedditStream")
    .master(SPARK_MASTER)
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")


df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "RedditStreamer")
    .load()
)


expr_cols = [f"CAST({col} AS STRING)" for col in df.columns]

df = df.selectExpr(*expr_cols)

df.writeStream.format("console").outputMode("append").start().awaitTermination()
