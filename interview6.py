#Data Structure Design:
#Design a class that supports both stack and queue operations using a single list. Implement methods for push, pop, enqueue, dequeue, and peek.
class StackQueue:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    def pop(self):
        if not self.data:
            return None
        return self.data.pop()
    def enqueue(self, item):
        self.data.append(item)
    def dequeue(self):
        if not self.data:
            return None
        return self.data.pop(0)
    def peek(self):
        if not self.data:
            return None
        return self.data[-1]
    def is_empty(self):
        return len(self.data) == 0
    def __str__(self):
        return str(self.data)
sq = StackQueue()
sq.push(10)
sq.push(20)
sq.push(30)
print("Stack after pushes:", sq)
print("Pop (stack):", sq.pop())
print("After pop:", sq)
sq.enqueue(40)
sq.enqueue(50)
sq.enqueue(60)
print("Queue after enqueues:", sq)
print("Dequeue (queue):", sq.dequeue())
print("After dequeue:", sq)
print("Peek:", sq.peek())

#Custom String Formatter:
#Write a function that takes a template string with placeholders and a dictionary, and returns the formatted string by replacing placeholders with dictionary values. Handle missing keys gracefully.
class SafeDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"
def safe_format(template: str, values: dict) -> str:
    return template.format_map(SafeDict(values))
template = "Hello {name}, you have {count} new messages. Your balance is {balance}."
data = {"name": "Alice", "count": 5}   
result = safe_format(template, data)
print(result)

#Multi-type Sorting:
#Given a list containing integers, floats, and strings, write a function that sorts the list so that all numbers come before strings, and numbers are sorted numerically, strings alphabetically.
def sort_numbers_and_strings(lst):
    return sorted(lst, key=lambda x: (isinstance(x, str), x))
mixed_list = [3, "banana", 1.5, "apple", 10, "cherry", 2]
sorted_list = sort_numbers_and_strings(mixed_list)
print("Original list:", mixed_list)
print("Sorted list:", sorted_list)

#Recursive List Flattening:
#Implement a recursive function that flattens a nested list of arbitrary depth into a single list.
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  
        else:
            flat_list.append(item)
    return flat_list
nested = [1, [2, [3, 4], 5], [6, 7], 8]
flat = flatten(nested)
print("Original nested list:", nested)
print("Flattened list:", flat)

#Dynamic Function Dispatcher:
#Create a function that takes a string command and arguments, and dispatches to the correct function (e.g., "add", "subtract", "multiply", "divide") using a dictionary of function references.
# --- Define the functions ---
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def command_dispatcher(command, *args):
    commands = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    func = commands.get(command)
    if func is None:
        return f"Unknown command: {command}"
    return func(*args)
print(command_dispatcher("add", 10, 5))        
print(command_dispatcher("subtract", 10, 5))   
print(command_dispatcher("multiply", 10, 5))   
print(command_dispatcher("divide", 10, 5))     

#Custom Exception Handling:
#Design a function that processes a list of values and raises custom exceptions for invalid types, negative numbers, or division by zero, and logs all errors.
import logging
logging.basicConfig(level=logging.ERROR, format='%(levelname)s:%(message)s')
class InvalidTypeError(Exception):
    pass
class NegativeNumberError(Exception):
    pass
class DivisionByZeroError(Exception):
    pass
def process_values(values):
    results = []
    for val in values:
        try:
            if not isinstance(val, (int, float)):
                raise InvalidTypeError(f"Invalid type: {val} ({type(val).__name__})")
            if val < 0:
                raise NegativeNumberError(f"Negative number: {val}")
            if val == 0:
                raise DivisionByZeroError("Division by zero attempted")
            result = 100 / val
            results.append(result)
        except (InvalidTypeError, NegativeNumberError, DivisionByZeroError) as e:
            logging.error(e)
        return results
values = [50, -10, 0, "abc", 25]
processed = process_values(values)
print("Processed results:", processed)

#Advanced List Comprehensions:
#Given a matrix (list of lists), use nested list comprehensions to extract the diagonal, transpose the matrix, and filter out rows containing negative numbers.
# --- Example matrix ---
matrix = [
    [1,  2,  3],
    [-4, 5,  6],
    [7,  8, -9]
]
diagonal = [matrix[i][i] for i in range(len(matrix))]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
positive_rows = [row for row in matrix if all(x >= 0 for x in row)]
print("Original matrix:")
for row in matrix:
    print(row)
print("\nDiagonal:", diagonal)
print("\nTranspose:")
for row in transpose:
    print(row)
print("\nRows without negative numbers:")
for row in positive_rows:
    print(row)

#Set and Dictionary Interactions:
#Write a function that takes a dictionary and a set, and returns a new dictionary containing only the key-value pairs where the key is in the set.
def filter_dict_by_keys(d, key_set):
    return {k: v for k, v in d.items() if k in key_set}
data = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_keep = {"a", "c", "e"}  # 'e' does not exist in data
filtered = filter_dict_by_keys(data, keys_to_keep)
print("Original dictionary:", data)
print("Filtered dictionary:", filtered)

#Memoized Recursive Fibonacci:
#Implement a recursive Fibonacci function with memoization to optimize performance. Compare its speed to the naive recursive approach.
import time
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
n = 35
start = time.time()
print("Naive Fibonacci:", fib_naive(n))
end = time.time()
print(f"Naive approach took {end - start:.4f} seconds")
start = time.time()
print("Memoized Fibonacci:", fib_memo(n))
end = time.time()
print(f"Memoized approach took {end - start:.6f} seconds")

#Custom Iterable Class:
#Create a class that implements the iterator protocol to iterate over its elements in reverse order.
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
my_list = [10, 20, 30, 40, 50]
rev_iter = ReverseIterator(my_list)
print("Reverse iteration:")
for item in rev_iter:
    print(item)

#Deep Copy with Custom Objects:
#Demonstrate deep copying of a list containing custom objects, ensuring that changes to copied objects do not affect the originals.
import copy

# --- Define a custom class ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# --- Original list of objects ---
people = [Person("Alice", 30), Person("Bob", 25)]

# --- Deep copy the list ---
people_copy = copy.deepcopy(people)

# --- Modify the copy ---
people_copy[0].name = "Charlie"
people_copy[1].age = 40

# --- Display results ---
print("Original list:", people)
print("Copied & modified list:", people_copy)

#Dynamic Attribute Access:
#Write a class that allows dynamic addition, deletion, and access of attributes using __getattr__, __setattr__, and __delattr__.
class DynamicAttributes:
    def __init__(self):
        self.__dict__['_attributes'] = {}
    def __getattr__(self, name):
        if name in self._attributes:
            return self._attributes[name]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    def __setattr__(self, name, value):
        self._attributes[name] = value
    def __delattr__(self, name):
        if name in self._attributes:
            del self._attributes[name]
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
obj = DynamicAttributes()
obj.name = "Alice"
obj.age = 30
print("Name:", obj.name)
print("Age:", obj.age)
del obj.age
try:
    print(obj.age)
except AttributeError as e:
    print("Error:", e)
obj.country = "USA"
print("Country:", obj.country)

#Functional Programming Challenge:
#Use map, filter, and reduce to process a list of numbers: double the even numbers, filter out numbers less than 10, and compute the product of the remaining numbers.
from functools import reduce
numbers = [1, 4, 5, 6, 7, 8, 2, 9]
doubled_evens = list(map(lambda x: x*2 if x % 2 == 0 else x, numbers))
filtered = list(filter(lambda x: x >= 10, doubled_evens))
product = reduce(lambda x, y: x * y, filtered, 1)
print("Original numbers:", numbers)
print("After doubling evens:", doubled_evens)
print("After filtering >= 10:", filtered)
print("Product of remaining numbers:", product)
