#50.Implement a distributed counter using Python.
import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def increment_counter(key, amount=1):
    # Atomic increment
    return r.incrby(key, amount)

def get_counter(key):
    return int(r.get(key) or 0)

# Usage
key = "global_counter"
print("Current counter:", get_counter(key))
increment_counter(key)
increment_counter(key, 5)
print("Updated counter:", get_counter(key))
