import json
import time
from datetime import datetime, timezone
from random import randint, uniform
from kafka import KafkaProducer


def create_event(i: int) -> dict:
    return {
        "event_id": f"evt-{i}",
        "customer_id": randint(1000, 9999),
        "amount": round(uniform(10, 500), 2),
        "event_type": "purchase",
        "event_time": datetime.now(timezone.utc).isoformat(),
    }


def run(bootstrap="localhost:9092", topic="transactions"):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    for i in range(1, 101):
        producer.send(topic, create_event(i))
        time.sleep(0.2)
    producer.flush()


if __name__ == "__main__":
    run()
