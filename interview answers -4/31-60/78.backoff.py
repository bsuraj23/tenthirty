#78.How do you handle retries and backoff in Python services?
import time, random
for attempt in range(1, max_attempts+1):
    try:
        do_work()
        break
    except TemporaryError:
        sleep = min(max_sleep, base * 2**(attempt-1))
        sleep *= random.uniform(0.5, 1.5)  # jitter
        time.sleep(sleep)
