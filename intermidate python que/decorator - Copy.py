import time

# Decorator function
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()             # start time
        result = func(*args, **kwargs)  # run the function
        end = time.time()               # end time
        print(f"Execution time of {func.__name__}: {end - start:.5f} seconds")
        return result
    return wrapper


# Example function using the decorator
@log_time
def slow_function():
    total = 0
    for i in range(1_000_000):   # some work
        total += i
    return total


# Run
print("Result:", slow_function())
