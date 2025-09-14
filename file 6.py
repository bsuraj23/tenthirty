#1custom String Formatter:
#Write a function that takes a template string with placeholders and a dictionary, and returns the formatted string by replacing placeholders with dictionary values. Handle missing keys gracefully.
def custom_format(template, values):
    class DefaultDict(dict):
        def __missing__(self, key):
            return f"{{{key}}}"  # keep placeholder if key missing
    return template.format_map(DefaultDict(values))
# Example usage
template = "Hello, {name}! You have {messages} new messages."
data = {"name": "Alice"}  # 'messages' key is missing
formatted = custom_format(template, data)
print(formatted)

#2Multi-type Sorting:
#Given a list containing integers, floats, and strings, write a function that sorts the list so that all numbers come before strings, and numbers are sorted numerically, strings alphabetically.
def multi_type_sort(lst):
    numbers = sorted([x for x in lst if isinstance(x, (int, float))])
    strings = sorted([x for x in lst if isinstance(x, str)])
    return numbers + strings
# Example usage
mixed = [3, "apple", 1.5, "banana", 2, "cherry", 0.5]
sorted_list = multi_type_sort(mixed)
print(sorted_list)
#3.Recursive List Flattening:
#Implement a recursive function that flattens a nested list of arbitrary depth into a single list.
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))  # recursive call
        else:
            result.append(item)
    return result
# Example usage
nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flat_list = flatten(nested_list)
print(flat_list)
#4.Dynamic Function Dispatcher:
#Create a function that takes a string command and arguments, and dispatches to the correct function (e.g., "add", "subtract", "multiply", "divide") using a dictionary of function references.
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else None
def dispatch(cmd,*args):
    return {"add":add,"sub":sub,"mul":mul,"div":div}.get(cmd, lambda *a: "Unknown")( *args)
# Example
print(dispatch("add",5,3))       # 8
print(dispatch("div",8,2))       # 4.0
print(dispatch("mod",5,2))       # Unknown
#5.Custom Exception Handling:
#Design a function that processes a list of values and raises custom exceptions for invalid types, negative numbers, or division by zero, and logs all errors.
def process_values(values):
    results = []
    for v in values:
        try:
            if type(v) not in (int, float):
                raise Exception(f"Invalid type: {v}")
            if v < 0:
                raise Exception(f"Negative number: {v}")
            if v == 0:
                raise Exception("Division by zero")
            results.append(100 / v)
        except Exception as e:
            print("Error:", e)
    return results
# Example
values = [50, -10, "abc", 0, 25]
print("Processed:", process_values(values))
#6.Advanced List Comprehensions:
#Given a matrix (list of lists), use nested list comprehensions to extract the diagonal, transpose the matrix, and filter out rows containing negative numbers.
matrix = [
    [1,  2,  3],
    [4, -5,  6],
    [7,  8,  9]
]
diagonal = [matrix[i][i] for i in range(len(matrix))]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
filtered_rows = [row for row in matrix if all(x >= 0 for x in row)]
print("Diagonal:", diagonal)
print("Transpose:", transpose)
print("Filtered Rows:", filtered_rows)

#7Set and Dictionary Interactions:
#Write a function that takes a dictionary and a set, and returns a new dictionary containing only the key-value pairs where the key is in the set.
def filter_dict_by_set(d, s):
    return {k: v for k, v in d.items() if k in s}
# Example usage
data = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = {"a", "c", "e"}
filtered = filter_dict_by_set(data, keys)
print(filtered)

#8Memoized Recursive Fibonacci:
#Implement a recursive Fibonacci function with memoization to optimize performance. Compare its speed to the naive recursive approach.
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
# Example usage
n = 10
print(f"Fibonacci({n}) =", fib_memo(n))
#9.Custom Iterable Class:
#Create a class that implements the iterator protocol to iterate over its elements in reverse order.
class ReverseIterable:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        self.index = len(self.data) - 1
        return self
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value
# Example usage
items = ReverseIterable([1, 2, 3, 4, 5])
for item in items:
    print(item, end=" ")
#10.List Partitioning:
#Write a function that partitions a list into n nearly equal parts and returns a list of lists.
def partition_list(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]
# Example usage
lst = [1,2,3,4,5,6,7,8,9,10]
parts = partition_list(lst, 3)
print(parts)
#11.Type-safe Function Decorator:
#Implement a decorator that checks the types of arguments passed to a function and raises a TypeError if they do not match the expected types.
def type_check(a_type, b_type):
    def decorator(func):
        def wrapper(a, b):
            if not isinstance(a, a_type):
                raise TypeError(f"First argument must be {a_type}")
            if not isinstance(b, b_type):
                raise TypeError(f"Second argument must be {b_type}")
            return func(a, b)
        return wrapper
    return decorator
# Example usage
@type_check(int, int)
def add(a, b):
    return a + b
print(add(5, 3))  
#12.Deep Copy with Custom Objects:
#Demonstrate deep copying of a list containing custom objects, ensuring that changes to copied objects do not affect the originals.
import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name}({self.age})"
people = [Person("Alice", 25), Person("Bob", 30)]
deep_copy = copy.deepcopy(people)
deep_copy[0].age = 99
print("Original:", people)    
print("Deep copy:", deep_copy) 
#13.Dynamic Attribute Access:
#Write a class that allows dynamic addition, deletion, and access of attributes using __getattr__, __setattr__, and __delattr__.
class DynamicAttributes:
    def __init__(self):
        self._attrs = {}  # store dynamic attributes
    def __getattr__(self, name):
        return self._attrs.get(name, f"{name} not found")
    def __setattr__(self, name, value):
        if name == "_attrs":          # allow normal initialization
            super().__setattr__(name, value)
        else:
            self._attrs[name] = value
    def __delattr__(self, name):
        if name in self._attrs:
            del self._attrs[name]
        else:
            print(f"{name} not found")
# Example
obj = DynamicAttributes()
obj.name = "Alice"   
obj.age = 25
print(obj.name, obj.age)  
del obj.age
print(obj.age)  
#14.Functional Programming Challenge:
#Use map, filter, and reduce to process a list of numbers: double the even numbers, filter out numbers less than 10, and compute the product of the remaining numbers.         
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_evens = map(lambda x: x*2 if x % 2 == 0 else x, numbers)
filtered = filter(lambda x: x >= 10, doubled_evens)
product = reduce(lambda x, y: x * y, filtered, 1)
print("Product:", product)







