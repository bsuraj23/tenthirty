#Decorators & Context Managers
#Decorator to log execution time
import time
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper
@log_time
def slow_function():
    time.sleep(1)
slow_function()

# #Decorator to count function calls
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} times")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
@count_calls
def greet():
    print("Hello!")
greet()
greet()
greet()

# #Decorator to allow only "admin"
def admin_only(func):
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print("Access denied!")
            return None
        return func(user, *args, **kwargs)
    return wrapper
@admin_only
def delete_database(user):
    print("Database deleted!")
delete_database("guest")   
delete_database("admin")   

# #Modules & Imports
# #Using if __name__ == "__main__":
def square(x):
    return x * x
def test_square():
    print("Testing square()...")
    assert square(5) == 25
    assert square(2) == 4
    print("All tests passed!")
if __name__ == "__main__":
    test_square()

# #Script using math library
import math
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))
print("Cosine of 0:", math.cos(0))


#Namespaces & Scope
#Demonstrate the LEGB Rule (Local → Enclosed → Global → Built-in)
x = "global"
def outer():
    x = "enclosed"
    def inner():
        x = "local"
        print("Inside inner:", x)  
    inner()
    print("Inside outer:", x)      
print("Global:", x)
outer()

#Modify a global variable using global
count = 0
def increment():
    global count
    count += 1
increment()
increment()
print("Global count:", count)  

#Modify an enclosed variable using nonlocal
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print("Inside inner:", x)
    inner()
    print("Inside outer:", x)
outer()

#Variable shadowing a built-in (sum)
def bad_sum():
    sum = 10  
    numbers = [1, 2, 3]
def good_sum():
    numbers = [1, 2, 3]
    total = sum(numbers)  
    print("Sum:", total)
good_sum()

#Name collisions between global & local variables
x = "global value"
def show_variable():
    x = "local value"
    print("Inside function:", x)
show_variable()
print("Outside function:", x)

#Functional Programming
#map() to square all elements
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)  

#filter() to extract even numbers
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  

#reduce() to find product of all numbers
from functools import reduce
nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)  

#Lambda function to sort tuples by second element
pairs = [(1, 5), (3, 1), (2, 4), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  

#Combine map, filter, reduce → sum of squares of even numbers
from functools import reduce
nums = [1, 2, 3, 4, 5, 6]
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums))
    )
print(result)  
