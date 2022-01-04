from kafka import KafkaProducer
import json

producer = KafkaProducer(
        bootstrap_servers = ['kafka:9092'],
        value_serializer = lambda x : json.dumps(x).encode('utf-8')
    )