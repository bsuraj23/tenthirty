import time
import threading

def task():
    for i in range(3):
        print(f"[{threading.current_thread().name}] Number:{i}")
        time.sleep(1)
print("Thread starting...")


t1=threading.Thread(target=task,name="T-1")
t2=threading.Thread(target=task,name="T-2")

t1.start()  # Starting the first thread
t2.start()  # Starting the second thread

t1.join()  # Wait for the first thread to finish
t2.join()  # Wait for the second thread to finish

print("All threads finished, program ends")