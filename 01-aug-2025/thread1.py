import time 
import threading 

def task1():
    time.sleep(3)
    print("task1 done")

def task2():
    print("task2 done ")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()