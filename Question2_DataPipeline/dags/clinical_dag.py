from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from kafka import KafkaConsumer
import json

def consume_clinical():
    consumer = KafkaConsumer(
        "clinical_trials",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="clinical-consumer",
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    for i, message in enumerate(consumer):
        print(f"[Clinical] {message.value}")
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
    dag_id="clinical_dag",
    default_args=default_args,
    schedule_interval="@weekly",  # weekly
    catchup=False,
    tags=["clinical", "kafka"],
) as dag:

    consume = PythonOperator(
        task_id="consume_clinical_data",
        python_callable=consume_clinical,
    )
