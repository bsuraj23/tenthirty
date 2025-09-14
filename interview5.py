#Custom Data Type Conversion:
#Write a function that takes a list of mixed data types (int, float, str, bool) and returns a dictionary with the count of each type.
def count_types(data_list):
    type_counts = {"int": 0, "float": 0, "str": 0, "bool": 0}
    for item in data_list:
        if isinstance(item, bool):      
            type_counts["bool"] += 1
        elif isinstance(item, int):
            type_counts["int"] += 1
        elif isinstance(item, float):
            type_counts["float"] += 1
        elif isinstance(item, str):
            type_counts["str"] += 1
        return type_counts
mixed_list = [1, 2.5, "hello", True, False, 42, "world", 3.14]
print(count_types(mixed_list))

#Dynamic Input Parser:
#Implement a function that reads a line of input and parses it into appropriate Python data types (int, float, bool, str) based on its content.
def parse_input(line):
    def parse_token(token):
        if token.lower() == "true":
            return True
        elif token.lower() == "false":
            return False
        try:
            return int(token)
        except ValueError:
            pass
        try:
            return float(token)
        except ValueError:
            pass
        return token
    return [parse_token(tok) for tok in line.split()]
user_line = input("Enter values separated by space: ")
parsed = parse_input(user_line)
print(parsed)
print([type(x) for x in parsed])   

#Type Conversion Utility:
#Write a function that takes a dictionary with string values and converts them to their most likely Python types (int, float, bool, str).
def convert_dict_values(data):
    def convert(value):
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        return value
    return {k: convert(v) for k, v in data.items()}
sample = {
    "age": "25",
    "height": "5.9",
    "active": "True",
    "name": "Alice",
    "zero": "0",
    "pi": "3.14159",
    "flag": "false"
}
converted = convert_dict_values(sample)
print(converted)
print({k: type(v) for k, v in converted.items()})

#Prime Number Generator:
#Write a generator function that yields all prime numbers up to n using nested loops and control statements.
def prime_generator(n):
    for num in range(2, n + 1):  
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1): 
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield num   
for p in prime_generator(30):
    print(p, end=" ")

#Custom List Class with Advanced Features:
#Implement a class that supports list operations (append, insert, remove, pop, reverse, sort) and also supports undo/redo of operations.
class UndoableList:
    def __init__(self, initial=None):
        self._list = list(initial) if initial else []
        self._history = []     
        self._redo_stack = []   
    def _save_state(self):
        self._history.append(self._list.copy())
        self._redo_stack.clear()
    def append(self, item):
        self._save_state()
        self._list.append(item)
    def insert(self, index, item):
        self._save_state()
        self._list.insert(index, item)
    def remove(self, item):
        self._save_state()
        self._list.remove(item)
    def pop(self, index=-1):
        self._save_state()
        return self._list.pop(index)
    def reverse(self):
        self._save_state()
        self._list.reverse()
    def sort(self):
        self._save_state()
        self._list.sort()
    def undo(self):
        if not self._history:
            print("Nothing to undo.")
            return
        self._redo_stack.append(self._list.copy())
        self._list = self._history.pop()
    def redo(self):
        if not self._redo_stack:
            print("Nothing to redo.")
            return
        self._history.append(self._list.copy())
        self._list = self._redo_stack.pop()
    def __repr__(self):
        return repr(self._list)
ulist = UndoableList([1, 2, 3])
print("Initial:", ulist)
ulist.append(4)
print("After append:", ulist)
ulist.remove(2)
print("After remove:", ulist)
ulist.undo()
print("After undo:", ulist)
ulist.redo()
print("After redo:", ulist)
ulist.reverse()
print("After reverse:", ulist)
ulist.sort()
print("After sort:", ulist)
ulist.undo()
print("Undo sort:", ulist)

#Set Operations:
#Write a function that takes two lists and returns their union, intersection, and difference using set operations.
def set_operations(list1, list2):
    set1, set2 = set(list1), set(list2)
    union = set1 | set2          
    intersection = set1 & set2   
    difference = set1 - set2     
    return union, intersection, difference
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]
u, i, d = set_operations(a, b)
print("Union:", u)
print("Intersection:", i)
print("Difference (A - B):", d)

#Type Casting Engine:
#Build a function that takes a list of values and a target type, and returns a new list with all values cast to the target type, handling exceptions gracefully.
def safe_cast_list(values, target_type):
    result = []
    for v in values:
        try:
            result.append(target_type(v))
        except (ValueError, TypeError):
            result.append(v)
    return result
data = ["10", "20.5", "hello", True, "42"]
print(safe_cast_list(data, int))    
print(safe_cast_list(data, float))  
print(safe_cast_list(data, str))    

#List Comprehension Challenge:
#Given a list of numbers, use list comprehensions to:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
double_evens = [x*2 if x % 2 == 0 else x for x in numbers]
greater_than_5 = [x for x in numbers if x > 5]
pairs = [(x, x**2) for x in numbers]
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [x for sublist in nested for x in sublist]
print("Squares:", squares)
print("Evens:", evens)
print("Odds:", odds)
print("Double evens:", double_evens)
print("Greater than 5:", greater_than_5)
print("Pairs:", pairs)
print("Flattened:", flattened)

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
@log_calls
def multiply(a, b):
    return a * b
multiply(6, 7)

#Deep Copy vs Shallow Copy Demonstration:
#Write code to demonstrate the difference between deep copy and shallow copy for nested lists.
import copy
original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)
print("Original:", original)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
original[0][0] = 99
print("\nAfter modifying original[0][0] = 99")
print("Original:", original)
print("Shallow Copy:", shallow_copy)  
print("Deep Copy:", deep_copy)        
original[1] = ["X", "Y", "Z"]
print("\nAfter replacing original[1] = ['X', 'Y', 'Z']")
print("Original:", original)
print("Shallow Copy:", shallow_copy)  
print("Deep Copy:", deep_copy)        

#Custom Implementation of Built-in Functions:
#Implement your own versions of max, min, and sum functions for lists without using the built-in ones.
def my_max(lst):
    if not lst:
        raise ValueError("my_max() arg is an empty list")
    maximum = lst[0]
    for item in lst[1:]:
        if item > maximum:
            maximum = item
    return maximum
def my_min(lst):
    if not lst:
        raise ValueError("my_min() arg is an empty list")
    minimum = lst[0]
    for item in lst[1:]:
        if item < minimum:
            minimum = item
    return minimum
def my_sum(lst):
    total = 0
    for item in lst:
        total += item
    return total
numbers = [3, 7, 2, 9, 5]
print("Numbers:", numbers)
print("My Max:", my_max(numbers))
print("My Min:", my_min(numbers))
print("My Sum:", my_sum(numbers))

#Advanced Control Flow:
#Write a function that takes a list of numbers and returns a new list with only the numbers that are not skipped by a custom rule (e.g., skip multiples of 3, break if a negative number is found, continue otherwise).
def filter_numbers(lst):
    result = []
    for num in lst:
        if num < 0:           
            break
        if num % 3 == 0:      
            continue
        result.append(num)    
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, -2, 8, 9]
print("Original:", numbers)
print("Filtered:", filter_numbers(numbers))

#Find all even numbers
#Square all odd numbers
#create a list of tuples (number, square) for numbers divisible by 3
#Set Membership and Manipulation:
#Implement a function that takes a string and returns a set of unique characters, then removes all vowels from the set.
def process_numbers(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    odd_squares = [x**2 for x in numbers if x % 2 != 0]
    div3_tuples = [(x, x**2) for x in numbers if x % 3 == 0]
    return evens, odd_squares, div3_tuples
def unique_chars_without_vowels(text):
    vowels = set("aeiouAEIOU")
    chars = set(text)         
    return chars - vowels     
nums = list(range(1, 11))
evens, odd_squares, div3_tuples = process_numbers(nums)
print("Numbers:", nums)
print("Even numbers:", evens)
print("Odd squares:", odd_squares)
print("Divisible by 3 tuples:", div3_tuples)
text = "Python Programming"
print("Unique chars without vowels:", unique_chars_without_vowels(text))
