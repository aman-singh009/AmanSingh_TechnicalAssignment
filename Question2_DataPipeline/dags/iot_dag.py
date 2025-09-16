from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from kafka import KafkaConsumer
import json

def consume_iot():
    consumer = KafkaConsumer(
        "iot_sensors",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="iot-consumer",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    for i, message in enumerate(consumer):
        print(f"[IoT] {message.value}")
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
    dag_id="iot_dag",
    default_args=default_args,
    schedule_interval="*/15 * * * *",  # every 15 minutes
    catchup=False,
    tags=["iot", "kafka"],
) as dag:

    consume = PythonOperator(
        task_id="consume_iot_data",
        python_callable=consume_iot,
    )

