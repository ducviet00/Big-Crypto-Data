docker exec -itd runner python kafka_create_topic.py > /tmp/kafka_create_topic.log 2>&1
docker exec -itd runner python crypto_crawler.py > /tmp/crypto_crawler.log 2>&1
docker exec -itd runner python crypto_consumer.py > /tmp/crypto_consumer.log 2>&1
docker exec -itd runner python reddit_praw.py > /tmp/reddit_praw.log 2>&1