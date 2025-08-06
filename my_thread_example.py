import threading
import time
def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)
my_thread = threading.Thread(target=print_numbers)
my_thread.start()
print("Main thread continues to run...")
my_thread.join()
print("Thread has finished.")


