import re
import logging
from abc import ABC, abstractmethod

# 1. Recursive Data Processing
def recursive_sum(data):
    total = 0
    if isinstance(data, dict):
        for v in data.values():
            total += recursive_sum(v)
    elif isinstance(data, list):
        for item in data:
            total += recursive_sum(item)
    elif isinstance(data, (int, float)):
        total += data
    return total

nested = {"a": 10, "b": [1, 2, {"c": 5, "d": [3, 4]}]}
print("Recursive sum:", recursive_sum(nested))


# 2. Regex-based Data Extraction
text = """
Emails: test@example.com, hello.world@company.org
Phones: +91-9876543210, 080-23456789
Dates: 2025-09-22, 22/09/2025, 09-22-2025
"""

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
phones = re.findall(r"(?:\+?\d{1,3}-)?\d{3,4}-\d{6,7}", text)
dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b", text)

print("Emails:", emails)
print("Phones:", phones)
print("Dates:", dates)

# 3. Custom Iterator for Fibonacci
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val

print("Fibonacci numbers:", [num for num in Fibonacci(7)])


# 4. Advanced Exception Handling
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: No permission to read file.")
    except Exception as e:
        print("Error reading file:", e)

read_file("non_existing.txt")

# 5. Assertions and Debugging
logging.basicConfig(filename="assert_log.txt", level=logging.ERROR)

def validate_age(age):
    try:
        assert age >= 0, "Age cannot be negative"
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        print("Invalid age:", e)

validate_age(-5)

# 6. Module & Package Management (Simulated)
# Normally we create separate files, but here we'll just use functions
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else None

print("Math Ops:", add(2,3), sub(5,3), mul(2,3), div(6,2))

# 7. Class Design with Multiple Constructors
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["age"])

p1 = Person("Alice", 25)
p2 = Person.from_string("Bob,30")
p3 = Person.from_dict({"name": "Charlie", "age": 28})
print(p1.name, p2.name, p3.name)

# 8. Inheritance & MRO
class A:
    def greet(self): print("Hello from A")
class B(A):
    def greet(self): 
        print("Hello from B")
        super().greet()
class C(A): 
    def greet(self): print("Hello from C")
class D(B, C): pass

d = D()
d.greet()
print("MRO:", D.mro())

# 9. Polymorphism with Abstract Base Class
class Shape(ABC):
    @abstractmethod
    def area(self): pass
    @abstractmethod
    def perimeter(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r
    def perimeter(self): return 2 * 3.14 * self.r

print("Circle area:", Circle(5).area())

# 10. Encapsulation & Property Decorators
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Balance cannot be negative")

acc = BankAccount(1000)
acc.balance = 500
print("Balance:", acc.balance)

# 11. Custom Exception Class
class InsufficientFunds(Exception): pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFunds("Not enough funds!")
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFunds as e:
    print("Error:", e)

# 12. Inner Classes & Composition
class Car:
    class Engine:
        def __init__(self, power): self.power = power
        def start(self): print(f"Engine with {self.power} HP started")

    def __init__(self, power):
        self.engine = Car.Engine(power)

car = Car(120)
car.engine.start()

# 13. Garbage Collection & Destructors
class Demo:
    def __init__(self): print("Object created")
    def __del__(self): print("Object destroyed")

obj = Demo()
del obj  

# 14. Function Aliasing & Higher Order Functions
def greet(name): return f"Hello {name}"
say_hello = greet
print(say_hello("Deepthi"))

def execute(func, value):
    return func(value)

print(execute(greet, "World"))

# 15. Interface Simulation
class InterfaceExample(ABC):
    @abstractmethod
    def show(self): pass

class Implementer(InterfaceExample):
    def show(self):
        print("Interface method implemented")

i = Implementer()
i.show()
