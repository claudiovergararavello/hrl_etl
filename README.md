# Helicopter Race League ETL

Este proyecto transforma archivos JSONL en AVRO utilizando Apache Beam, orquestado diariamente por Apache Airflow. Al finalizar, se notifica a Kafka.

## Cómo ejecutar

1. Clonar el repositorio y abrir en VSCode con Devcontainers.
2. Levantar los servicios:

```
docker-compose up -d
```