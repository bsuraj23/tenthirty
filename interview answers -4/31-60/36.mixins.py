#36.How do you implement mixins in Python?
# Step 1: Define a Mixin
class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

# Step 2: Define a main class
class Worker:
    def work(self):
        print("Working...")

# Step 3: Combine Worker with LoggerMixin
class LoggingWorker(Worker, LoggerMixin):
    pass

lw = LoggingWorker()
lw.work()      # Working...
lw.log("Task completed")  # [LOG]: Task completed