import threading
import time

def task():
    time.sleep(5)             #it will take time to runs 5 seconds (that we mentioned)
    print("Thread task finished!")

t = threading.Thread(target=task)
t.start()  #it start the function task


t.join()     #it executes first "thread task finished" then "main program done!", join waits for task function
print("Main program done!")             # to finish it and then runs the "Main program done!"

