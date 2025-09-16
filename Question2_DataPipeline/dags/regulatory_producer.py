from kafka import KafkaProducer
import json, time, random
from faker import Faker

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    report = {
        "report_id": fake.uuid4(),
        "department": random.choice(["R&D", "Manufacturing", "Finance"]),
        "status": random.choice(["Compliant", "Non-Compliant"]),
        "timestamp": fake.iso8601()
    }
    producer.send("reg_reports", report)
    print("Sent:", report)
    time.sleep(2592000)  # every 30 days (monthly)
