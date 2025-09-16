from kafka import KafkaConsumer
import json

# List of all topics
topics = [
    "erp_sales",
    "iot_sensors",
    "clinical_trials",
    "social_media",
    "regulatory_reports",
    "finance_data"
]

# Create consumer
consumer = KafkaConsumer(
    *topics,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="multi-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Listening for messages on all 6 topics...")

# Read messages
for message in consumer:
    print(f"[{message.topic}] {message.value}")
