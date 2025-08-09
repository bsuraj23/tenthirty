
import simple_module.py


def greet():
    print("Hello from simple module!")


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
