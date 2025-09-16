from kafka import KafkaProducer
import json, time, random
from faker import Faker

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    sale = {
        "order_id": fake.uuid4(),
        "customer": fake.name(),
        "amount": round(random.uniform(100, 1000), 2),
        "timestamp": fake.iso8601()
    }
    producer.send("erp_sales", sale)
    print("Sent:", sale)
    time.sleep(2)
