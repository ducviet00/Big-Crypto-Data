FROM docker.io/bitnami/spark:3

USER root

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /opt/bitnami/spark/app
