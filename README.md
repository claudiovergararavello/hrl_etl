# Helicopter Race League ETL

Este proyecto transforma un archivo JSONL con los datos de la Helicopter Race League y lo transforma a formato AVRO utilizando Apache Beam. Todo esto orquestado diariamente por Apache Airflow que al finalizar el Pipeline de Beam notifica a un tópico de Apache Kafka.

*Nota: Se hizo un pequeño cambio al esquema avro para el campo Timestamp Unix:* 

### Antes
```
    {"name": "Timestamp_unix", "type":{
           "type": "long",
           "logicalType": "timestamp-millis"
        }
    }
```
### Ahora
```
    {"name": "Timestamp_unix", "type": "long"},

```

## Pasos de ejecución

1. Clonar el repositorio y abrir en VSCode con Devcontainers: Para esto es necesario instalar la extensión *Dev Containers* de Microsoft y abrir el contenedor usando *Ctrl + Shift + P → Dev Containers: Rebuild Container*.

2. Una vez ejecutado el DevContainer procedera a levantar los servicios de Apache Airflow y ejecutar el DAG diariamente.

3. Cuando se ejecuta el DAG, en la carpeta *output* obtendremos el archivo *.avro* con los datos convertidos.

4. Es posible instalar una interfaz gráfica para visualizar las notificaciones de los tópicos. Para este caso accederemos al contenedor de kafka usando una terminal y ejecutaremos:
```
docker exec -it hrl_etl_devcontainer-kafka-1 bash
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic etl_notifications --from-beginning
```
*Nota: Opcionalmente podemos acceder a la termina del contenedor usando Docker Deskptop y solo ejecutar el comando de kafka.*

## Conversión de JSON a AVRO en terminal
Para ejecutar la conversión de los registros del archivo *fan_engagement.jsonl* a AVRO se usa un Direct Runner definido a continuación:
```
python beam_pipeline/process_json_to_avro.py input/fan_engagement.jsonl output/ beam_pipeline/schema.avsc
``` 
