# Big-Crypto-Data
Visualize and suggestion crypto prices
![img](https://i.imgur.com/VxeVV1R.png)

## Setup
~~~bash
docker build -t custom_spark:0.1 .
docker-compose up -d
bash run.sh
~~~

## Spark Cluster
- 1 Master and 2 Workers

![img](https://i.imgur.com/mftylB4.png)

## Spark Streaming
![img](https://i.imgur.com/BW1MSTp.png)

## Kafka
- 3 topics: `_Sentiment`, `_TradingData`, `_RedditStreamer`

![img](https://i.imgur.com/tw6gRmP.png)

## ElasticSearch
- 2 replicas - 2.5gb total

![img](https://i.imgur.com/wOXVFEE.png)

## Kibana
![img](https://i.imgur.com/yQ4BP5B.png)
