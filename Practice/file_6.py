from functools import reduce
import copy

#Data Structure Design - Stack + Queue in one class
class StackQueue:
    def __init__(self):
        self.data = []

    def push(self, value): 
        self.data.append(value)

    def pop(self):  
        return self.data.pop() if self.data else None

    def enqueue(self, value):  
        self.data.append(value)

    def dequeue(self):  
        return self.data.pop(0) if self.data else None

    def peek(self):  
        return self.data[-1] if self.data else None


#Custom String Formatter 
def custom_formatter(template, values):
    result = template
    for key, val in values.items():
        result = result.replace(f"{{{key}}}", str(val))
    import re
    result = re.sub(r"\{.*?\}", "", result)
    return result


#Multi-type Sorting 
def multi_type_sort(lst):
    numbers = sorted([x for x in lst if isinstance(x, (int, float))])
    strings = sorted([x for x in lst if isinstance(x, str)])
    return numbers + strings


#Recursive List Flattening
def flatten_list(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


#Dynamic Function Dispatcher
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else None

def dispatcher(command, a, b):
    operations = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
    func = operations.get(command)
    return func(a, b) if func else None


#Custom Exception Handling
class InvalidTypeError(Exception): pass
class NegativeNumberError(Exception): pass
class DivisionByZeroError(Exception): pass

def process_values(values):
    results = []
    for v in values:
        try:
            if not isinstance(v, (int, float)):
                raise InvalidTypeError(f"Invalid type: {v}")
            if v < 0:
                raise NegativeNumberError(f"Negative number: {v}")
            results.append(10 / v if v != 0 else (_ for _ in ()).throw(DivisionByZeroError("Division by zero")))
        except (InvalidTypeError, NegativeNumberError, DivisionByZeroError) as e:
            print(f"Error: {e}")
    return results


#Advanced List Comprehensions
def matrix_operations(matrix):
    diagonal = [matrix[i][i] for i in range(min(len(matrix), len(matrix[0])))]
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    no_negative_rows = [row for row in matrix if all(x >= 0 for x in row)]
    return diagonal, transpose, no_negative_rows


#Set and Dictionary Interactions
def filter_dict_by_set(d, s):
    return {k: v for k, v in d.items() if k in s}


#Memoized Recursive Fibonacci
def memoized_fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = memoized_fib(n-1, memo) + memoized_fib(n-2, memo)
    return memo[n]

def naive_fib(n):
    if n <= 1:
        return n
    return naive_fib(n-1) + naive_fib(n-2)


#Custom Iterable Class 
class ReverseIterable:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        self.index = len(self.data)
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


#List Partitioning
def partition_list(lst, n):
    k, m = divmod(len(lst), n)
    parts = []
    start = 0
    for i in range(n):
        end = start + k + (1 if i < m else 0)
        parts.append(lst[start:end])
        start = end
    return parts


#Type-safe Function Decorator
def type_check(expected_types):
    def decorator(func):
        def wrapper(*args):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Expected {expected}, got {type(arg)}")
            return func(*args)
        return wrapper
    return decorator

@type_check((int, int))
def add_numbers(a, b):
    return a + b


#Deep Copy with Custom Objects
class CustomObject:
    def __init__(self, value):
        self.value = value

def demonstrate_deep_copy():
    obj1 = CustomObject(10)
    obj2 = CustomObject(20)
    original = [obj1, obj2]
    copied = copy.deepcopy(original)
    copied[0].value = 99
    return [(o.value, c.value) for o, c in zip(original, copied)]


#Dynamic Attribute Access
class DynamicObject:
    def __init__(self):
        self.__dict__["_attributes"] = {}

    def __getattr__(self, name):
        return self._attributes.get(name, None)

    def __setattr__(self, name, value):
        self._attributes[name] = value

    def __delattr__(self, name):
        if name in self._attributes:
            del self._attributes[name]


#Functional Programming Challenge
def functional_challenge(numbers):
    doubled = map(lambda x: x*2, filter(lambda x: x % 2 == 0, numbers))
    filtered = filter(lambda x: x >= 10, doubled)
    product = reduce(lambda x, y: x * y, filtered, 1)
    return product
