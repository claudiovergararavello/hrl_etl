from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from kafka import KafkaProducer
import json

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def notify_kafka():
    producer = KafkaProducer(bootstrap_servers='kafka:9092',
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    message = {
        "event_type": "data_processing_completed",
        "data_entity": "FanEngagement",
        "status": "success",
        "location": "/workspace/output/",
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source_system": "fan_engagement_etl_dag"
    }
    producer.send("etl_notifications", message)
    producer.flush()

with DAG(
        "fan_engagement_dag",
         start_date=datetime(2025, 6, 1),
         schedule_interval="@daily",
         catchup=False
        ) as dag:

    run_beam = BashOperator(
        task_id="run_beam_pipeline",
        bash_command="python /workspace/beam_pipeline/process_json_to_avro.py /workspace/input/fan_engagement.jsonl /workspace/output/ /workspace/beam_pipeline/schema.avsc"
    )

    notify = PythonOperator(
        task_id="notify_kafka",
        python_callable=notify_kafka
    )

    run_beam >> notify
