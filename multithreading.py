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
