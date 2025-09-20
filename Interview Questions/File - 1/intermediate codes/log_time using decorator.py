import time
def log_time(fun):
    def wrapper(*args,**kwargs):  
        start=time.time()
        result=fun(*args,**kwargs)
        end=time.time()
        print(f'Execution time of {fun.__name__}:{end-start:.4f}seconds') #here the 4f is the 4float values
        return result                                                              # after 2 seconds delay
    return wrapper

@log_time
def slow_function():
    time.sleep(2)   #here this stopping 2 seconds delay
    print("Finished work!")

slow_function()