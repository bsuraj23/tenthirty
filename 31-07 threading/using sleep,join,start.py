import threading
import time

def print_numbers():
    for i in range(3):
        print(f"[{threading.current_thread().name}] Number: {i}")
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2=threading.Thread(target=print_numbers, name="Thread-2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Main thread: All threads finished.")