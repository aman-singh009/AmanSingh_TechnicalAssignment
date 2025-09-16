from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    sensor = {
        "machine_id": random.randint(1, 10),
        "temperature": round(random.uniform(20, 100), 2),
        "pressure": round(random.uniform(1, 10), 2),
        "timestamp": time.time()
    }
    producer.send("iot_sensors", sensor)
    print("Sent:", sensor)
    time.sleep(900)  # every 15 minutes
