from pyspark.sql import SparkSession
import pyspark.sql.functions as SF
from pyspark.sql.types import StructType, StructField, StringType, FloatType
from nltk.sentiment.vader import SentimentIntensityAnalyzer

SPARK_MASTER = "spark://spark:7077"

sia = SentimentIntensityAnalyzer()

@SF.udf
def sentiment_analysis(message):
    return sia.polarity_scores(message)["compound"]

spark = (
    SparkSession.builder.appName("RedditStream")
    .master(SPARK_MASTER)
    .getOrCreate()
)
spark.sparkContext.setLogLevel("WARN")


df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "_RedditStreamer")
    .load()
)


data_schema = StructType(
    [
        StructField("date", StringType(), False),
        StructField("author", StringType(), False),
        StructField("body", StringType(), False),
    ]
)


expr_cols = [f"CAST({col} AS STRING)" for col in df.columns]

df = df.selectExpr(*expr_cols)

json_options = {"dateFormat" : "yyyy-MM-dd HH:mm:ss.SSS"}

df = df.withColumn("value", SF.from_json(SF.col("value"), data_schema))

df = df.withColumn("author", df.value["author"])
df = df.withColumn("body", df.value["body"])
sentiment_analysis_udf = SF.udf(sentiment_analysis, FloatType())
df = df.withColumn("polarity", sentiment_analysis(df.body))

df.drop()
# rdd = df.rdd.map(lambda row: (row.timestamp, row.author, row.body, sentiment_analysis(row)))

# df = rdd.toDF(["timestamp","author","body", "polarity"])


df.writeStream.format("console").outputMode("append").start().awaitTermination()