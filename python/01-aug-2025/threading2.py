import time 
import threading

def task1():
    time.sleep(2)
    print("helper thread")

print("i starting the job main thread")


t = threading.Thread(target = task1)

t.start()

print("i will be working while the helper is busy")