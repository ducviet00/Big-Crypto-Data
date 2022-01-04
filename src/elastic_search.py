from elasticsearch import Elasticsearch
from datetime import datetime

elastic = Elasticsearch(
    ['es01:9200', 'es02:9200', 'es03:9200'],
    # sniff before doing anything
    sniff_on_start=True,
    # refresh nodes after a node fails to respond
    sniff_on_connection_fail=True,
    # and also every 60 seconds
    sniffer_timeout=60
)

