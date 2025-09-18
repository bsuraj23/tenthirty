# Write a decorator that logs the execution time of a function.
import time
from functools import wraps

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # run the function
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.4f} seconds")
        return result
    return wrapper


# Example usage
@log_execution_time
def slow_function():
    time.sleep(2)
    print("Finished slow function")

slow_function()
