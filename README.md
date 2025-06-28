# Helicopter Race League ETL

Este proyecto transforma archivos JSONL en AVRO utilizando Apache Beam, orquestado diariamente por Apache Airflow. Al finalizar, se notifica a Kafka.

## Cómo ejecutar

1. Clonar el repositorio y abrir en VSCode con Devcontainers: Para esto es necesario instalar la extensión *Dev Containers* de Microsoft y abrir el contenedor usando * Ctrl + Shift + P → Dev Containers: Reopen in Container*.

2. Una vez creado el DevContainer procedemos a levantar los servicios de Apache Airflow usando:

```
airflow standalone
```

## Conversión de JSON a AVRO
Para ejecutar la conversión de los registros del archivo *fan_engagement.jsonl* a AVRO se usa un Direct Runner definido a continuación:
```
python beam_pipeline/json_to_avro.py \
  --runner DirectRunner \
  --input input/input.jsonl \
  --output output/output.avro
``` 