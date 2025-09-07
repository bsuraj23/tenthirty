from multiprocessing
import _posixsubprocess
import time

def worker(n):
    print(f'worker {n} started')
    time.sleep(2)
    print(f'Worker {n} finished')
    print(f'Worker {n} finished')
    p.start()  # Start the new process
    p.join() # Waits for the process to finish
    print('Main process continued')

