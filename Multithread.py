#1.Creating a thread
import threading

def task():
    print("This is a thread function.")

# Create the thread
thread = threading.Thread(target=task)

print("Thread is created.")

#2.Starting a thread
import threading

def task():
    print("Thread has started and is running...")

thread = threading.Thread(target=task)
thread.start()  # Start the thread

print("Thread is started.")

#3.Using join() method
import threading
import time

def task():
    print("Thread task is running...")
    time.sleep(2)
    print("Thread task completed.")

thread = threading.Thread(target=task)
thread.start()
thread.join()

print("Main program continues after thread has finished.")