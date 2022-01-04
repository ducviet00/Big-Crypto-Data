from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(bootstrap_servers="kafka:9092")


topic_names = ["_TradingData", "_RedditStreamer", "_Sentiment"]

topic_list = []

for topic in topic_names:
    topic_list.append(NewTopic(name=topic, num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)
print("DONE")
