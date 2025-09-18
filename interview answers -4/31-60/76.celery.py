#76.How do you implement a distributed task queue in Python (like Celery)?
## pip install dramatiq redis
import dramatiq
from dramatiq.brokers.redis import RedisBroker
broker = RedisBroker(url="redis://localhost:6379/0")
dramatiq.set_broker(broker)

@dramatiq.actor(max_retries=3)
def add(x, y):
    return x + y
