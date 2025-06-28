FROM python:3.11-bullseye

# Kafka CLI tools
RUN apt-get update && apt-get install -y \
    default-jre \
    wget \
    netcat \
    git \
    nano \
    curl \
    build-essential \
    librdkafka-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace