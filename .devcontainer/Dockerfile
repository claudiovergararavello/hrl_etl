FROM python:3.11-slim

# Apache Beam con DirectRunner
RUN pip install apache-beam[gcp]==2.53.0

# Airflow
ENV AIRFLOW_HOME=/opt/airflow
RUN pip install apache-airflow==2.9.1 apache-airflow-providers-apache-kafka

# Kafka CLI tools
RUN apt-get update && apt-get install -y \
    default-jre wget netcat git nano curl

# Para zona horaria y UTF-8
ENV TZ=America/Santiago
ENV LANG=C.UTF-8
