
#Example 3: module_with_class.py
 
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello,", self.name)
# main.py

P= Person("Archana")
P.say_hello()

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

# math_utils.py

"""
A simple Python module for basic math operations.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def factorial(n):
    """Return the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # Example usage
    print("Add: ", add(5, 3))
    print("Subtract: ", subtract(5, 3))
    print("Multiply: ", multiply(5, 3))
    print("Divide: ", divide(5, 3))
    print("Factorial: ", factorial(5))

