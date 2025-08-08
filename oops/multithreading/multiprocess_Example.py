import multiprocessing
import time

def squares():
    for i in range(1,4):
        print(f"[{multiprocessing.current_process().name}],square of {i} is {i*i}")
        time.sleep(1)

p1=multiprocessing.Process(target=squares,name="P-1")
p2=multiprocessing.Process(target=squares,name="P-2")

# To join the process, we need to ensure the code is protected
# by the if __name__ == "__main__": guard.

if __name__ == "__main__":
    # This guard prevents the code from being run on import
    
    print("Main Program starting...")
    p1.start()  # Starting the first process
    p2.start()  # Starting the second process 
    
    p1.join()  # Wait for the first process to finish
    p2.join()
    
    print("All processes finished, program ends")
    print("Main Program ends")
