from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from kafka import KafkaConsumer
import json

def consume_social():
    consumer = KafkaConsumer(
        "social_media",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="social-consumer",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    for i, message in enumerate(consumer):
        print(f"[Social] {message.value}")
        if i >= 5:
            break

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 9, 15),
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="social_dag",
    default_args=default_args,
    schedule_interval="@daily",  # daily
    catchup=False,
    tags=["social", "kafka"],
) as dag:

    consume = PythonOperator(
        task_id="consume_social_data",
        python_callable=consume_social,
    )
