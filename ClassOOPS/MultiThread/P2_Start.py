import threading

def task():
    print("Thread has started!")

# Create and start the thread
my_thread = threading.Thread(target=task)
my_thread.start()  # Starts running in parallel
