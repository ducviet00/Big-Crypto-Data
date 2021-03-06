echo "Creating Kafka topics"
docker exec -itd runner python kafka_create_topic.py > /tmp/kafka_create_topic.log 2>&1
sleep 2
echo "Starting crypto crawler"
docker exec -itd runner python crypto_crawler.py > /tmp/crypto_crawler.log 2>&1
sleep 2
echo "Starting crypto consumer"
docker exec -itd runner python crypto_consumer.py > /tmp/crypto_consumer.log 2>&1
sleep 2 
echo "Starting reddit streamer"
docker exec -itd runner python reddit_praw.py > /tmp/reddit_praw.log 2>&1
sleep 2
echo "Starting Spark Streaming"
docker exec -it runner spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 spark_streaming.py 