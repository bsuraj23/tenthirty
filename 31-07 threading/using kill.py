import multiprocessing
import time

def sqr_of_numbers():
    for i in range(3):
        print(f"[{multiprocessing.current_process().name}] square of {i} is {i*i}")
        time.sleep(2)

p1=multiprocessing.Process(target=sqr_of_numbers, name="Process-1")
p2=multiprocessing.Process(target=sqr_of_numbers, name="Process-2")

p1.start()
p2.start()

p1.join()
p2.join()

print("Main process: all subprocess are completed")
