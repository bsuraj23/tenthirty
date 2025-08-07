import threading
import time

def task():
    print("Thread is running")
    time.sleep(2)
    print("Thread finished")

t1=threading.Thread(target=task)
t1.start()  # Starting the thread

t1.join()  # Wait for thread to finish
print("Program waiting for thread to finish")