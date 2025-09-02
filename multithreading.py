import multiprocessing

def task():
    print("Task running in process:", multiprocessing.current_process().name)

if __name__ == "__main__":
    p = multiprocessing.Process(target=task)
    p.start()
    p.join()
#example 2
import multiprocessing
import time

def worker(name):
    for i in range(3):
        print(f"{name} working...")
        time.sleep(1)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=("Process 1",))
    p2 = multiprocessing.Process(target=worker, args=("Process 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main process finished")
# examples 3
import threading
import time

# Define thread class for downloading
class DownloadThread(threading.Thread):
    def __init__(self, file_name):
        threading.Thread.__init__(self)
        self.file_name = file_name

    def run(self):
        print(f"Started downloading: {self.file_name}")
        time.sleep(2)  # Simulate time delay
        print(f"Finished downloading: {self.file_name}")

# Define thread class for processing
class ProcessThread(threading.Thread):
    def __init__(self, task_name):
        threading.Thread.__init__(self)
        self.task_name = task_name

    def run(self):
        print(f"Started processing: {self.task_name}")
        time.sleep(3)  # Simulate processing time
        print(f"Finished processing: {self.task_name}")

# Create download threads
d1 = DownloadThread("file1.txt")
d2 = DownloadThread("file2.txt")

# Create processing threads
p1 = ProcessThread("resize image")
p2 = ProcessThread("convert PDF")

# Start all threads
d1.start()
d2.start()
p1.start()
p2.start()

# Wait for all threads to finish
d1.join()
d2.join()
p1.join()
p2.join()

print("\n All tasks completed!")



# multi threading
# without threading
import time

def task1():
    for i in range(3):
        print("Task 1:", i)
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2:", i)
        time.sleep(1)

# Run one after another
task1()
task2()

# with threading
import threading
import time

def task1():
    for i in range(3):
        print("Task 1:", i)
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2:", i)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

# Example1
import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Numbers: {i}")
        time.sleep(1)

def print_letters():
    for ch in "ABCDE":
        print(f"Letters: {ch}")
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread finished")

# using class
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        for i in range(3):
            print(f"{self.name} - Step {i}")
            time.sleep(self.delay)

t1 = MyThread("Thread-1", 1)
t2 = MyThread("Thread-2", 2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads completed")


#Multiple Threads in a Loop
import threading
import time

def worker(id):
    print(f"Thread-{id} starting")
    time.sleep(1)
    print(f"Thread-{id} finished")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads done")

#Using threading.Lock to Avoid Mixed Output
import threading
import time

lock = threading.Lock()

def safe_print(name):
    for i in range(3):
        with lock:  # Only one thread prints at a time
            print(f"{name} says hello {i}")
        time.sleep(0.5)

t1 = threading.Thread(target=safe_print, args=("Thread-A",))
t2 = threading.Thread(target=safe_print, args=("Thread-B",))

t1.start()
t2.start()

t1.join()
t2.join()

#ThreadPoolExecutor (Easier Thread Management)
from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"{name} starting")
    time.sleep(1)
    print(f"{name} finished")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(task, "Task-1")
    executor.submit(task, "Task-2")
    executor.submit(task, "Task-3")



