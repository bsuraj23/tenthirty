import threading

def task():
    print("Thread is running")
def add():
    print("Adding numbers")

# Creating threads
t1= threading.Thread(target=task)
print("Thread 1 started")
t1.start()  # Starting the thread 

t2= threading.Thread(target=add)
print("Thread 2 started")
t2.start()  # Starting the second thread