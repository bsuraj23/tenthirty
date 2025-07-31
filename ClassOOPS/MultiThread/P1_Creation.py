import threading

# Define the task (function) for the thread
def task():
    print("Thread is running!")

# Create the thread
my_thread = threading.Thread(target=task)

# Thread is created but not yet started
print("Thread created:", my_thread)
