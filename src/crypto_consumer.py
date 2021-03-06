from elasticsearch import Elasticsearch, helpers
from kafka import KafkaConsumer
import time
import json

es = Elasticsearch(
    ['es01:9200', 'es02:9200'],
    # sniff before doing anything
    sniff_on_start=True,
    # refresh nodes after a node fails to respond
    sniff_on_connection_fail=True,
    # and also every 60 seconds
    sniffer_timeout=60
)


consumer = KafkaConsumer(bootstrap_servers=['kafka:9092'], auto_offset_reset='earliest', consumer_timeout_ms=1000)
consumer.subscribe(['_TradingData'])

for message in consumer:
    message = message.value.decode('utf-8')
    candles = json.loads(message)
    index_ = "candlesticks"
    response = helpers.bulk(es, candles, index=index_, request_timeout=200)
    time.sleep(0.01)