#42.Implement a thread-safe queue in Python.
from queue import Queue
import threading
import time

q = Queue()

def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(0.1)

def consumer():
    for _ in range(5):
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()
        time.sleep(0.2)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
