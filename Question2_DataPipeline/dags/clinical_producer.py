from kafka import KafkaProducer
import json, time, random
from faker import Faker

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    trial = {
        "trial_id": fake.uuid4(),
        "patient": fake.name(),
        "drug": random.choice(["DrugA", "DrugB", "DrugC"]),
        "outcome": random.choice(["Success", "Failure", "Ongoing"]),
        "timestamp": fake.iso8601()
    }
    producer.send("clinical_trials", trial)
    print("Sent:", trial)
    time.sleep(604800)  # every 7 days (weekly)
