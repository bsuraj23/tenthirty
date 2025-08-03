import threading 
import time
def task(name):
    print(f"Thread{"katli"} starting")
    time.sleep(2)
    print(f"Thread {"kaju"} finished")

# Create threads
t1 = threading.Thread(target=task,args=("kaju",))
t2 = threading.Thread(target=task,args=("katli",))

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Both threads completed.")