#Set Operations:
#Write a function that takes two lists and returns their union, intersection, and difference using set operations.
def set_ops(list_a, list_b):
    a, b = set(list_a), set(list_b)
    return {
        "union": a | b,
        "intersection": a & b,
        "difference_a_minus_b": a - b
    }

# example
print(set_ops([1,2,3,3], [2,3,4]))

#Type Casting Engine:
#Build a function that takes a list of values and a target type, and returns a new list with all values cast to the target type, handling exceptions gracefully.
def cast_list(values, target_type):
    results = []
    errors = []
    for i, v in enumerate(values):
        try:
            results.append(target_type(v))
        except Exception as e:
            results.append(None)
            errors.append((i, v, str(e)))
    return results, errors

# example
vals = ["10", "3.5", "x", True]
casted, errs = cast_list(vals, int)
print(casted)  
print(errs)

#List Comprehension Challenge:
#Given a list of numbers, use list comprehensions to:
nums = list(range(1, 16))

evens = [n for n in nums if n % 2 == 0]
squared_odds = [n**2 for n in nums if n % 2 == 1]
div3_tuples = [(n, n**2) for n in nums if n % 3 == 0]

print(evens)         
print(squared_odds)  
print(div3_tuples) 

#Find all even numbers
#Square all odd numbers
#Create a list of tuples (number, square) for numbers divisible by 3
#Set Membership and Manipulation:
#Implement a function that takes a string and returns a set of unique characters, then removes all vowels from the set.
def unique_no_vowels(s):
    vowels = set("aeiouAEIOU")
    unique_chars = set(s)
    unique_chars -= vowels
    return unique_chars

print(unique_no_vowels("Hello, world!"))

#Function Decorator for Logging:
#Write a decorator that logs the arguments and return value of any function it wraps.
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# usage
@log_calls
def add(a, b):
    return a + b

add(2, 3)

#Deep Copy vs Shallow Copy Demonstration:
#Write code to demonstrate the difference between deep copy and shallow copy for nested lists.
import copy

nested = [[1, 2], [3, 4]]
shallow = list(nested)          
deep = copy.deepcopy(nested)

# mutate inner list in shallow copy
shallow[0].append(99)
print("original after shallow change:", nested)  

# mutate inner list in deep copy
deep[1].append(88)
print("original after deep change:", nested)

#Custom Implementation of Built-in Functions:
#Implement your own versions of max, min, and sum functions for lists without using the built-in ones.
def my_max(values):
    if not values:
        raise ValueError("my_max() arg is an empty sequence")
    it = iter(values)
    best = next(it)
    for v in it:
        if v > best:
            best = v
    return best

def my_min(values):
    if not values:
        raise ValueError("my_min() arg is an empty sequence")
    it = iter(values)
    best = next(it)
    for v in it:
        if v < best:
            best = v
    return best

def my_sum(values):
    total = 0
    for v in values:
        total += v
    return total

print(my_max([3,1,4,2]))  
print(my_min([3,1,4,2]))  
print(my_sum([3,1,4,2]))

#Advanced Control Flow:
#Write a function that takes a list of numbers and returns a new list with only the numbers that are not skipped by a custom rule (e.g., skip multiples of 3, break if a negative number is found, continue otherwise).
def custom_filter(nums):
    result = []
    for n in nums:
        if n < 0:
            break          
        if n % 3 == 0:
            continue        
        result.append(n)
    return result

print(custom_filter([1, 2, 3, 4, 6, 5, -1, 7]))