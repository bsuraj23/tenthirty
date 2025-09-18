#1Recursive Data Processing:
#Write a recursive function to traverse and sum all numeric values in a nested dictionary or list structure of arbitrary depth.
def sum_numbers(data):
    total = 0
    if isinstance(data, dict):
        for value in data.values():
            total += sum_numbers(value)
    elif isinstance(data, list):
        for item in data:
            total += sum_numbers(item)
    elif isinstance(data, (int, float)):
        total += data
    return total
# Example usage
nested = {
    "a": 1,
    "b": [2, 3, {"c": 4}],
    "d": {"e": 5, "f": [6, 7]}
}
print("Total sum:", sum_numbers(nested))

#2Regex-based Data Extraction:
#Given a block of text, use regular expressions to extract all valid email addresses, phone numbers, and dates in various formats.
import re
def extract_data(text):
    emails = re.findall(r'\S+@\S+', text)
    phones = re.findall(r'\d{3}[-\s]?\d{3}[-\s]?\d{4}', text)
    dates = re.findall(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}', text)
    return emails, phones, dates
text = """
Email: user@example.com, admin@site.org
Phone: 123-456-7890, 987 654 3210
Dates: 12/05/2023, 1-1-22
"""
emails, phones, dates = extract_data(text)
print("Emails:", emails)
print("Phones:", phones)
print("Dates:", dates)
#3.Custom Iterator for Fibonacci Sequence:
#Implement a class that generates Fibonacci numbers up to n using the iterator protocol (__iter__ and __next__).
class Fibonacci:
    def __init__(self, n):
        self.n = n  # upper limit
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a > self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value
# Example usage
for num in Fibonacci(10):
    print(num, end=" ")
#4.Advanced Exception Handling:
#Design a function that reads a file, parses its contents, and handles multiple exceptions (e.g., file not found, invalid format, permission error) with custom error messages.
def read_and_parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            numbers = [int(x) for x in content.split(',')]
            print("Numbers:", numbers)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("No permission to read the file.")
    except ValueError:
        print("Invalid format in file.")
# Example usage
read_and_parse_file("data.txt")
#5.Assertions and Debugging:
#Write a function that validates input data using assertions and logs assertion failures to a file for debugging.
def validate_data(data):
    try:
        assert isinstance(data, list), "Data must be a list"
        assert len(data) > 0, "List cannot be empty"
        assert all(isinstance(x, int) for x in data), "All items must be integers"
        print("Data is valid!")
    except AssertionError as e:
        with open("error_log.txt", "a") as file:
            file.write(f"Error: {e}\n")
        print("Validation failed. See error_log.txt")
# Example usage
validate_data([1, 2, 'a'])
validate_data("not a list")
validate_data([])
#6.Class Design with Multiple Constructors:
#Implement a class with multiple ways to instantiate objects (e.g., from string, from dictionary, from individual arguments) using class methods as alternative constructors.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split(",")
        return cls(name, int(age))
    @classmethod
    def from_dict(cls, data_dict):
        return cls(data_dict["name"], data_dict["age"])
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
p1 = Person("Alice", 25)
p2 = Person.from_string("Bob,30")
p3 = Person.from_dict({"name": "Charlie", "age": 35})
p1.show()
p2.show()
p3.show()
#7.Inheritance and Method Resolution Order (MRO):
#Design a class hierarchy with multiple inheritance. Demonstrate how Python resolves method calls using MRO and the super() function.
class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()
class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()
class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()
# Create an object of class D
d = D()
d.greet()
# Show the Method Resolution Order
print("MRO:", [cls.__name__ for cls in D.__mro__])
#8.Polymorphism with Abstract Base Classes:
#Create an abstract base class for geometric shapes with abstract methods for area and perimeter. Implement concrete subclasses for circle, rectangle, and triangle.
from abc import ABC, abstractmethod
import math
# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
# Concrete class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
# Concrete class for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
# Concrete class for Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
# Using the classes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
#9.Encapsulation and Property Decorators:
#Write a class with private attributes and use property decorators to provide controlled access and validation for those attributes.
class Person:
    def __init__(self, name, age):
        self._name = name      # private attribute
        self._age = age        # private attribute
    # Getter for name
    @property
    def name(self):
        return self._name
    # Setter for name with validation
    @name.setter
    def name(self, value):
        if not value:
            print("Name cannot be empty!")
        else:
            self._name = value
    # Getter for age
    @property
    def age(self):
        return self._age
    # Setter for age with validation
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value
# Using the class
person = Person("Alice", 30)
print("Name:", person.name)
print("Age:", person.age)
# Try setting invalid values
person.name = ""
person.age = -5
# Set valid values
person.name = "Bob"
person.age = 40
print("Updated Name:", person.name)
print("Updated Age:", person.age)
#10.Custom Exception Class:
#Define a custom exception class for invalid operations in a banking application. Use it to handle errors such as insufficient funds or invalid account numbers.
# Custom exception
class BankingError(Exception):
    pass
# Bank account class
class BankAccount:
    def __init__(self, account_number, balance):
        if account_number <= 0:
            raise BankingError("Invalid account number.")
        self.account_number = account_number
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise BankingError("Insufficient funds.")
        self.balance -= amount
        print("Withdraw successful.")
# Example usage
try:
    account = BankAccount(123, 100)
    account.withdraw(200)
except BankingError as e:
    print("Error:", e)
#11.Inner Classes and Composition:
#Implement a class that contains an inner class for managing related data (e.g., a Car class with an inner Engine class). Demonstrate composition and data sharing.
class Car:
    def __init__(self, model, engine_power):
        self.model = model
        self.engine = self.Engine(engine_power)  # Composition: Car has an Engine
    def show(self):
        print(f"Car Model: {self.model}")
        print(f"Engine Power: {self.engine.power} HP")
    # Inner class
    class Engine:
        def __init__(self, power):
            self.power = power
# Using the classes
car = Car("Toyota", 150)
car.show()
#12.Garbage Collection and Destructors:
#Write a class that logs messages when objects are created and destroyed. Demonstrate how Python’s garbage collector works with object references.
import gc
class MyObject:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created.")
    def __del__(self):
        print(f"{self.name} destroyed.")
obj1 = MyObject("Object1")
obj2 = MyObject("Object2")
del obj1
gc.collect()
print("End of program.")
#13.Function Aliasing and Higher-Order Functions:
#Show how to assign functions to variables, pass them as arguments, and return them from other functions. Use this to implement a simple plugin system.
# Plugin functions
def shout(text):
    return text.upper() + "!"
def whisper(text):
    return text.lower() + "..."
# Higher-order function
def apply(text, plugin):
    return plugin(text)
plugin = shout   # function aliasing
print(apply("hello", plugin))  # Output: HELLO!
plugin = whisper
print(apply("HELLO", plugin))  # Output: hello...
#14.Interface Simulation:
#Simulate interfaces in Python using abstract base classes. Enforce that subclasses implement specific methods and demonstrate runtime checks.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car started")
def operate(vehicle):
    if not isinstance(vehicle, Vehicle):
        raise TypeError("Must implement Vehicle interface")
    vehicle.start()
car = Car()
operate(car)  # Output: Car started








