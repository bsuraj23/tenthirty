import multiprocessing

def task():
    print("Process started!")

process = multiprocessing.Process(target=task)
process.start()  # Starts running the task in a separate process
