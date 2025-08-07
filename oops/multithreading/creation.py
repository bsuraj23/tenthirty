import threading

def task():
    print("Thread is running")
def add():
    print("Adding numbers")

# Creating threads
t1= threading.Thread(target=task)
#thread1 is created but not started yet
print("Thread 1 created")
t2= threading.Thread(target=add)
#thread2 is created but not started yet
print("Thread 2 created")