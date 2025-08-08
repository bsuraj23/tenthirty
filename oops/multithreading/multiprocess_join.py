"""If there's no if __name__ == "__main__": guard, 
it runs all code again — including process.start()
which leading to infinite recursion or bootstrapping issues.

"""
import multiprocessing
import time

def task():
    print("Process is running...")
    time.sleep(2)
    print("Process finished")

#To join the process, we need to ensure the code is protected
# by the if __name__ == "__main__": guard.

if __name__ == "__main__":
    
    print("Main Program starting...")
    p1=multiprocessing.Process(target=task)
    p1.start()  # Starting the process
    p1.join()  # Wait for the process to finish
    print("Main Program waiting for process to finish")
    