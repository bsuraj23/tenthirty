# Check if a string is a palindrome
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("madam"))  
print(is_palindrome("hi"))
print(is_palindrome("racecar")) 
print(is_palindrome("dad"))

#remove duplicates from list
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates(['a', 'b', 'a', 'c', 'b']))

#merge two dictionaries
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged
print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
print(merge_dicts({'k': 10}, {'i': 20, 'j': 30}))

#find the frequency of each character in a string
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
print(char_frequency("hi how are you doing"))
print(char_frequency("saipavankumar"))

#own version of `max()` without using the built-in function.
def custom_max(lst):
    if not lst:
        return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum
print(custom_max([11, 5, 625, 86786, 498, 212, 789, 7898, 124]))
print(custom_max([-10, -54, -65, -1, -498, -212, -789, -7898, -124]))

#Reverse a list **in place** without using `[::-1]` or `reverse()`
def reverse_list_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
print(reverse_list_in_place([1, 2, 3, 4, 5,8,9,10,100]))
print(reverse_list_in_place(['a', 'b', 'c', 'd', 'i','k','l']))

#flatten a nested list (e.g. `[[1,2],[3,4]] → [1,2,3,4]`).
def flatten(nested_lst):
    flat_list = []
    for sublist in nested_lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list
print(flatten([[1, 2], [3, 4]]))
print(flatten([['a', 'b'], ['c', 'd']]))

#Given a string, count the number of vowels and consonants.
def count_vowels_consonants(o):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in o:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count
print(count_vowels_consonants("saipavankumarbabbusasiuday"))

#Find the second largest number in a list.
def second_largest(lst):
    first = second = float('-inf')
    for number in lst:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None
print(second_largest([14,78,456,789,123,147,258,369,753,159,845]))

#Rotate a list by `k` elements (circular shift).
def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle rotation greater than list length
    return lst[-k:] + lst[:-k]
print(rotate_list([5,6,7,8,9], 2))
print(rotate_list(['a', 'w', 'r', 'o', 'i'], 3))

# Print the Fibonacci sequence up to `n` terms.
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(10))

# Write a program to print a multiplication table for a number.
def multiplication_table(num, terms=10):
    table = []
    for i in range(1, terms + 1):
        table.append(f"{num} x {i} = {num * i}")
    return table
print(multiplication_table(7))

# Write code to find all prime numbers up to `n`.
def primes_up_to_n(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print(primes_up_to_n(1000))

#Implement a function to check if two strings are anagrams.
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(are_anagrams("sai", "pavan"))
print(are_anagrams("listen", "silent"))

#Find all numbers between 1 and 100 divisible by both 3 and 5.
def divisible_by_3_and_5():
    result = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            result.append(num)
    return result
print(divisible_by_3_and_5())

#Write a function that takes \*args and \*\*kwargs and prints them separately.
def print_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
print_args_kwargs(1, 2, 3, name="sai", age=22)

#Implement a recursive function to calculate factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(20))

# Implement a recursive function to compute Fibonacci numbers.
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
print(fibonacci_recursive(54))

#Write a function that accepts a list and returns a new list with only unique elements.
def unique_elements(lst):
    return list(set(lst))
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))

#Write a function that returns the sum of digits of a number.
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
print(sum_of_digits(123455))

#Create a class `BankAccount` with methods `deposit`, `withdraw`, and `check_balance`.
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid withdrawal amount")

    def check_balance(self):
        return self.balance
account = BankAccount()
account.deposit(1000)
account.withdraw(500)
print("Current Balance:", account.check_balance())

#Implement inheritance with a base class `Shape` and derived classes `Circle` and `Rectangle` with an `area()` method.
import math
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())

#Implement a class with a **static method** to check if a number is even.
class NumberUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0
print(NumberUtils.is_even(10))

#Create a class `Car` that tracks the number of cars created using a **class variable**.
class Car:
    car_count = 0
    def __init__(self, model):
        self.model = model
        Car.car_count += 1
    @classmethod
    def get_car_count(cls):
        return cls.car_count
car1 = Car("Toyota")
car2 = Car("Honda") 
print("Total Cars:", Car.get_car_count())

#Override the `__str__` method in a class to display custom output.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
person = Person("Sai", 22)
print(person)

#Create a custom iterator class that generates square numbers up to `n`.
class SquareNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.n:
            square = self.current ** 2
            self.current += 1
            return square
        else:
            raise StopIteration
squares = SquareNumbers(100)
for square in squares:
    print(square)   

#Write a generator function that yields even numbers up to `n`.
def even_numbers(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num
for even in even_numbers(100):
    print(even) 

#Implement a generator that yields Fibonacci numbers.
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for fib in fibonacci_generator(20):
    print(fib)

#Write a generator that reads a large file line by line.
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
for line in read_large_file('large_file.txt'):
    print(line)

#Create a generator that yields prime numbers up to `n`.
def prime_generator(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
for prime in prime_generator(100):
    print(prime)




#Handle Division by Zero with try-except
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")


#Custom Exception NegativeNumberError
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative number is not allowed!")
    else:
        print("Valid number:", num)

# Example
try:
    check_number(-5)
except NegativeNumberError as e:
    print("Caught Exception:", e)

   # Retry Division 3 Times
def safe_divide(a, b):
    attempts = 0
    while attempts < 3:
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Division by zero. Try again.")
            b = int(input("Enter a new denominator: "))
            attempts += 1
    return "Failed after 3 attempts"

# Example
print(safe_divide(10, 0))


#Handle Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")


#Decorator to Log Execution Time
import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def slow_function():
    time.sleep(2)
    print("Done!")

slow_function()

#Decorator to Count Function Calls
def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def greet(name):
    print(f"Hello, {name}!")

greet("sashi")
greet("janu")

#Decorator to Allow Only "admin"
def admin_only(func):
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print("Access Denied! Only admin can run this function.")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@admin_only
def delete_database(user):
    print("Database deleted!")

delete_database("guest")   
delete_database("admin")   

#Context Manager for File Handling

#Context Manager to Temporarily Change Directory
import os

class ChangeDirectory:
    def __init__(self, new_path):
        self.new_path = new_path
        self.old_path = os.getcwd()

    def __enter__(self):
        os.chdir(self.new_path)

    def __exit__(self, exc_type, exc_value, traceback):
        os.chdir(self.old_path)

# Example
print("Current:", os.getcwd())
with ChangeDirectory("/tmp"):
    print("Inside context:", os.getcwd())
print("Back to:", os.getcwd())

# Modules & Imports

#Namespaces & Scope
#Demonstrating the LEGB Rule
x = "global x"   # Global

def outer():
    x = "enclosed x"  
    def inner():
        x = "local x"  
        print("Inside inner:", x)
    inner()
    print("Inside outer:", x)

outer()
print("In global:", x)

#Modify a Global Variable with global
count = 0   # Global variable

def increment():
    global count
    count += 1
    print("Inside function:", count)

increment()
increment()
print("Outside function:", count)

#Modify an Enclosed Variable with nonlocal
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        print("Inside inner:", x)
    inner()
    inner()
    print("Inside outer:", x)

outer()

#Shadowing a Built-in Function (e.g., sum)
def wrong_sum_example():
    sum = 10  
    print("Shadowed sum:", sum)

def fixed_sum_example():
    total = sum([1, 2, 3]) 
    print("Correct sum:", total)

wrong_sum_example()
fixed_sum_example()

#Global vs Local Variable Name Collision
value = "global value"

def show_value():
    value = "local value"  
    print("Inside function:", value)

show_value()
print("Outside function:", value)

# Data Handling
#Read a Text File and Count Words
def count_words(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()
            words = text.split()
            print("Word count:", len(words))
    except FileNotFoundError:
        print("em ledu dolla!")

# Example
count_words("sample.txt")

#Write a List of Numbers to a File (One per Line)

#Serialize Dictionary to JSON and Back
import json

data = {"name": "kirikiri", "age": 88, "city": "kazakistan"}

# Serialize to JSON
json_str = json.dumps(data)
print("Serialized:", json_str)

# Deserialize back to dictionary
new_data = json.loads(json_str)
print("Deserialized:", new_data)

# Functional Programming
#Use map() to Square All Elements
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

#Use filter() to Extract Even Numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

#Use reduce() to Find Product of All Numbers
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

#Sort Tuples by Second Element
data = [(1, 3), (2, 1), (4, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted:", sorted_data)

#Combine map, filter, and reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)

print("Sum of squares of even numbers:", result)


