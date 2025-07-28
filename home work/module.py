#Example 1: simple_module.py

def greet():
    print("Hello from simple module!")
  # main.py
simple_module.greet() 

# Example 2: math_module.py with alias

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y
# main.py

import math_module as mm

print("Sum:", mm.add(10, 5))
print("Product:", mm.multiply(4, 3))


# Example 3: module_with_class.py
 

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello,", self.name)
# main.py

p = Person("Archana")
p.say_hello()

# Example 4: module_with_constants.py
PI = 3.14159
# main.py

radius = 5
area = PI * radius * radius
print("Area of circle:", area)

# Example 5: module_with_functions.py

def square(x):
    return x * x
# main.py

print("Square of 6 is:", square(6))


