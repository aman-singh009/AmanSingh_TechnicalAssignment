from kafka import KafkaProducer
import json, time, random
from faker import Faker

fake = Faker()
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    tweet = {
        "user": fake.user_name(),
        "text": fake.sentence(),
        "sentiment": random.choice(["Positive", "Negative", "Neutral"]),
        "timestamp": fake.iso8601()
    }
    producer.send("social_media", tweet)
    print("Sent:", tweet)
    time.sleep(86400)  # every 24 hours (daily)
