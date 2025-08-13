import multiprocessing
import time

def task():
    print("Process Working")
    time.sleep(3)
    print("Process finished")

process=multiprocessing.Process(target=task)
process.start()

process.join()
print("Main program waited for process to finish")

