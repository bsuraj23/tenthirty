#To Terminate the process use process.kill()

import multiprocessing

def task():
    print("This is a separate process!")

# Create a process
process = multiprocessing.Process(target=task)
print(f"Process is started: {process}")

process.kill()  