#49.Implement a rate limiter in Python.
import time
import threading

class RateLimiter:
    def __init__(self, max_calls, period):
        """
        max_calls: maximum number of allowed calls
        period: time window in seconds
        """
        self.max_calls = max_calls
        self.period = period
        self.calls = 0
        self.lock = threading.Lock()
        self.reset_time = time.time() + period

    def allow(self):
        with self.lock:
            current_time = time.time()
            # Reset counter if period has passed
            if current_time > self.reset_time:
                self.calls = 0
                self.reset_time = current_time + self.period

            if self.calls < self.max_calls:
                self.calls += 1
                return True
            else:
                return False

# -------------------------
# Usage Example
# -------------------------
limiter = RateLimiter(max_calls=5, period=10)  # 5 calls per 10 seconds

for i in range(10):
    if limiter.allow():
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Blocked")
    time.sleep(1)


