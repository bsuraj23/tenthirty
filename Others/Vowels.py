# text = "Nothing is permanent it written in Gita and Quran"
# values = "aeiouAEIOU"

# for char in text:
#     if char in values:
#         print(char)

import threading 
import time
def task(name):
    print(f"Thread{name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")

# Create threads
t1 = threading.Thread(target=task,args=("A",))
t2 = threading.Thread(target=task,args=("B",))

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

print("Both threads completed.")