#1-Creating a Thread
import threading

def print_numbers():
    for i in range(5):
        print("Number:", i)

# Create thread
thread = threading.Thread(target=print_numbers)

# 2. Starting a Thread
import threading

def greet():
    print("Hello from thread!")

# Create and start thread
thread = threading.Thread(target=greet)
thread.start()
# 3. Using join() Method

import threading
import time

def task():
    time.sleep(1)
    print("Task completed.")

# 2-Create thread
thread = threading.Thread(target=task)
thread.start()

# Wait for thread to finish
thread.join()

print("Main program finished.")
# 3- Full Multithreading Example
import threading
import time

def task1():
    for i in range(3):
        print("Task 1 - Count:", i)
        time.sleep(1)

def task2():
    for i in range(3):
        print("Task 2 - Count:", i)
        time.sleep(1)

#4 Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Both tasks completed.")

import threading
import time

def print_numbers():
    for i in range(5):
        print("Number:", i)
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print("Letter:", letter)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print("Done with both threads.")
