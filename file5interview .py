#file 5# Custom Data Type Conversion:
#Write a function that takes a list of mixed data types (int, float, str, bool) and returns a dictionary with the count of each type.
def count_data_types(mixed_list):
    type_count = {}
    for item in mixed_list:
        item_type = type(item).__name__  # Get the type name as a string
        if item_type in type_count:
            type_count[item_type] += 1
        else:
            type_count[item_type] = 1
    return type_count
# Example usage:
mixed_list = [1, 2.5, "hello", True, False, 3, "world", 4.5]
result = count_data_types(mixed_list)
print(result)
#2Dynamic Input Parser:
#Implement a function that reads a line of input and parses it into appropriate Python data types (int, float, bool, str) based on its content.
def dynamic_input_parser(input_line):
    input_line = input_line.strip()
    # Check for boolean
    if input_line.lower() == "true":
        return True
    elif input_line.lower() == "false":
        return False
    # Check for integer
    try:
        return int(input_line)
    except ValueError:
        pass
    # Check for float
    try:
        return float(input_line)
    except ValueError:
        pass
    # Otherwise, return as string
    return input_line
# Example usage:
inputs = ["123", "45.67", "true", "False", "hello"]
parsed = [dynamic_input_parser(i) for i in inputs]
print(parsed)
#3String Manipulation Suite:
#Given a string, write functions to:
def to_uppercase(s):
    return s.upper()
def to_lowercase(s):
    return s.lower()
def reverse_string(s):
    return s[::-1]
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
def remove_spaces(s):
    return s.replace(" ", "")
def capitalize_words(s):
    return s.title()
# Example usage:
text = "Hello World"
print("Original:", text)
print("Uppercase:", to_uppercase(text))
print("Lowercase:", to_lowercase(text))
print("Reversed:", reverse_string(text))
print("Vowel Count:", count_vowels(text))
print("Without Spaces:", remove_spaces(text))
print("Capitalized Words:", capitalize_words(text))
#4Type Conversion Utility:
#Write a function that takes a dictionary with string values and converts them to their most likely Python types (int, float, bool, str).
def convert_dict(d):
    def parse(v):
        v = v.strip().lower()
        if v=="true": return True
        if v=="false": return False
        try: return int(v)
        except: 
            try: return float(v)
            except: return v
    return {k: parse(v) for k,v in d.items()}
# Example
data = {"age":"25","height":"5.7","student":"true","name":"Katyayini"}
print(convert_dict(data))
#5Prime Number Generator:
#Write a generator function that yields all prime numbers up to n using nested loops and control statements.
def prime_generator(n):
    for num in range(2, n+1):
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            yield num
# Example usage
for prime in prime_generator(20):
    print(prime, end=" ")
#6Custom List Class with Advanced Features:
#Implement a class that supports list operations (append, insert, remove, pop, reverse, sort) and also supports undo/redo of operations.
class AdvancedList:
    def __init__(self):
        self.data = []
        self.history = []      # stores past states for undo
        self.redo_stack = []   # stores states for redo
    def _save_state(self):
        self.history.append(self.data.copy())
        self.redo_stack.clear()  # clear redo after new operation
    def append(self, x):
        self._save_state()
        self.data.append(x)
    def insert(self, i, x):
        self._save_state()
        self.data.insert(i, x)
    def remove(self, x):
        self._save_state()
        self.data.remove(x)
    def pop(self, i=-1):
        self._save_state()
        return self.data.pop(i)
    def reverse(self):
        self._save_state()
        self.data.reverse()
    def sort(self):
        self._save_state()
        self.data.sort()
    def undo(self):
        if self.history:
            self.redo_stack.append(self.data.copy())
            self.data = self.history.pop()
        else:
            print("Nothing to undo")
    def redo(self):
        if self.redo_stack:
            self.history.append(self.data.copy())
            self.data = self.redo_stack.pop()
        else:
            print("Nothing to redo")
    def __repr__(self):
        return repr(self.data)
# Example usage
lst = AdvancedList()
lst.append(3)
lst.append(1)
lst.append(2)
print("Original:", lst)
lst.sort()
print("After sort:", lst)
lst.undo()
print("After undo:", lst)
lst.redo()
print("After redo:", lst)
lst.reverse()
print("After reverse:", lst)
#7Set Operations:
#Write a function that takes two lists and returns their union, intersection, and difference using set operations.
def set_operations(list1, list2):
    set1, set2 = set(list1), set(list2)
    union = set1 | set2           # or set1.union(set2)
    intersection = set1 & set2    # or set1.intersection(set2)
    difference = set1 - set2      # elements in list1 not in list2
    return union, intersection, difference
# Example usage
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
u, i, d = set_operations(list1, list2)
print("Union:", u)
print("Intersection:", i)
print("Difference:", d)
#8Type Casting Engine:
#Build a function that takes a list of values and a target type, and returns a new list with all values cast to the target type, handling exceptions gracefully.
def type_cast_list(values, target_type):
    result = []
    for v in values:
        try:
            result.append(target_type(v))
        except (ValueError, TypeError):
            result.append(None)  # or keep original v if you prefer
    return result
# Example usage
values = ["1", "2.5", "abc", True]
print(type_cast_list(values, int))   # [1, 2, None, 1]
print(type_cast_list(values, float)) # [1.0, 2.5, None, 1.0]
print(type_cast_list(values, str))   # ['1', '2.5', 'abc', 'True']
#9List Comprehension Challenge:
#Given a list of numbers, use list comprehensions to:
#Find all even numbers
#Square all odd numbers
#Create a list of tuples (number, square) for numbers divisible by 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
squared_odds = [x**2 for x in numbers if x % 2 != 0]
div_by_3 = [(x, x**2) for x in numbers if x % 3 == 0]
print("Evens:", evens)
print("Squared Odds:", squared_odds)
print("Divisible by 3 tuples:", div_by_3)
#10 Set Membership and Manipulation:
#Implement a function that takes a string and returns a set of unique characters, then removes all vowels from the set.
def unique_consonants(s):
    vowels = set("aeiouAEIOU")
    chars = set(s)            # unique characters
    return chars - vowels     # remove vowels
# Example usage
text = "Hello World"
result = unique_consonants(text)
print(result)
#11 Function Decorator for Logging:
#rite a decorator that logs the arguments and return value of any function it wraps.
def log(func):
    def wrapper(*a, **kw):
        print(f"{func.__name__} called with {a}, {kw}")
        r = func(*a, **kw)
        print(f"{func.__name__} returned {r}")
        return r
    return wrapper
@log
def add(a, b): return a + b
add(3, 5)
#12 Deep Copy vs Shallow Copy Demonstration:
#Write code to demonstrate the difference between deep copy and shallow copy for nested lists.
import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0][0] = 100
print("Original:", original)   # [[100, 2], [3, 4]]
print("Shallow copy:", shallow) # [[100, 2], [3, 4]] → affected
print("Deep copy:", deep)       # [[1, 2], [3, 4]] → unchanged
#13 Custom Implementation of Built-in Functions:
#Implement your own versions of max, min, and sum functions for lists without using the built-in ones.
def my_max(lst):
    m = lst[0]
    for x in lst: 
        if x>m: m=x
    return m
def my_min(lst):
    m = lst[0]
    for x in lst: 
        if x<m: m=x
    return m
def my_sum(lst):
    total=0
    for x in lst: total+=x
    return total
# Example
nums = [4,2,9,7,1]
print(my_max(nums), my_min(nums), my_sum(nums))  # 9 1 23
#14 Advanced Control Flow:
#Write a function that takes a list of numbers and returns a new list with only the numbers that are not skipped by a custom rule (e.g., skip multiples of 3, break if a negative number is found, continue otherwise).
def filter_numbers(numbers):
    result = []
    for num in numbers:
        if num < 0:        # break if negative
            break
        if num % 3 == 0:   # skip multiples of 3
            continue
        result.append(num)
    return result
# Example usage
nums = [1, 2, 3, 4, 5, 6, -1, 7, 8]
filtered = filter_numbers(nums)
print(filtered)


