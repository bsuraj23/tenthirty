#custom iterator for fobonacci numbers  
class fib:
    def __init__(self,n):
        self.n=n 
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<=0:
            raise StopIteration
        self.n-=1
        val=self.a
        self.a,self.b=self.b,self.a+self.b
        return val
for x in fib(5):
        print(x)
#decorator to log execution time
#A decorator is a function that wraps another function to extend its behavior without modifying the function itself. In this case, we’ll create a decorator that logs how long a function takes to run.
import time

def execution_time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@execution_time_logger
def compute_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total

result = compute_sum(1000000)
print("Sum =", result)
  #generator for even numbers up to N
def even_gen(n):
    for i in range(0,n+1,2):
        yield i
print(list(even_gen(10)))
#flattern a nested list
nested=[[1,2],[3,4]]
flat=[x for sub in nested for x in sub]
print(flat)
#
nested=[[1,2],[3,4]]
flat=sum(nested,[])
print(flat)
# #count word frequencies in a file
# from collections import Counter
# import os
# file_path = 'file.txt'
# if not os.path.exists(file_path):
#     print(f"Error: {file_path} not found.")
# else:
#     with open(file_path) as f:
#         words = f.read().split()
#     freq = Counter(words)
#     for word, count in freq.items():
#         print(f"{word}: {count}")
#context manager for filr operations
# class MyFile:
#     def __init__(self, filename, mode):
#         self.file = open(filename, mode)

#     def __enter__(self):
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()

# # Usage
# with MyFile('file.txt', 'r') as file:
#     print(file.read())
    #suares of even numbers using map and filter
nums= [1,2,3,4,5,6]
evens=filter(lambda x:x%2==0,nums)
squares=list(map(lambda x:x*x, evens))
print(squares)
#import custom module
# mymodule.py

def greet(name):
    return f"Hello, {name}!"

