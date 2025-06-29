# Helicopter Race League ETL

Este proyecto transforma un archivo JSONL con los datos de la Helicopter Race League y lo transforma a formato AVRO utilizando Apache Beam. Todo esto orquestado diariamente por Apache Airflow que al finalizar el Pipeline de Beam notifica a un tópico de Apache Kafka.

## Cómo ejecutar

1. Clonar el repositorio y abrir en VSCode con Devcontainers: Para esto es necesario instalar la extensión *Dev Containers* de Microsoft y abrir el contenedor usando * Ctrl + Shift + P → Dev Containers: Rebuild Container*.

2. Una vez creado el DevContainer procedemos a levantar los servicios de Apache Airflow usando:

```
airflow standalone
```

## Conversión de JSON a AVRO
Para ejecutar la conversión de los registros del archivo *fan_engagement.jsonl* a AVRO se usa un Direct Runner definido a continuación:
```
python beam_pipeline/process_json_to_avro.py input/fan_engagement.jsonl output/ beam_pipeline/schema.avsc
``` 