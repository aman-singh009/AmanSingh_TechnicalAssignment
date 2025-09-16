from kafka import KafkaProducer
import json, time, random
from faker import Faker

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers="localhost:29092",  # keep external listener
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    finance = {
        "account_id": fake.iban(),
        "closing_balance": round(random.uniform(1000, 100000), 2),
        "currency": "USD",
        "timestamp": fake.iso8601()
    }
    producer.send("finance_data", finance)
    print("Sent:", finance)
    time.sleep(86400)  # every 24 hours (daily)
