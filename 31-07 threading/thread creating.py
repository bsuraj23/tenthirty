import threading
def task():
    print("Thread is running!")
def add():
    print("Add  is running")

my_thread=threading.Thread(target=task)
print("Thread created:",my_thread)
my_thread.start()