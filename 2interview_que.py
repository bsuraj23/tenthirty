#1Custom Iterator for Fibonacci Numbers
# class FibonacciIterator:
#     def __init__(self, limit):
#         self.limit = limit  # how many numbers to generate
#         self.a, self.b = 1, 2
#         self.count = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count >= self.limit:
#             raise StopIteration
#         value = self.a
#         self.a, self.b = self.b, self.a + self.b
#         self.count += 1
#         return value
# # Example usage
# for num in FibonacciIterator(7):
#     print(num, end=" ")  


#2Function Decorator for Logging Execution Time
import time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper
@log_execution_time
def slow_function():
    time.sleep(1)
    return "Done"
print(slow_function())


#3Generator for Even Numbers up to N
def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i
print(list(even_numbers(10)))  


#4Flatten a Nested List
def flatten_list(nested_list):
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat
print(flatten_list([[1, 2], [3, 4]]))  
