✅ What Is a "Static Class"?
A static class:
Has only @staticmethod or @classmethods
Does not require instantiation (i.e., you never do obj = ClassName())
Python doesn't have a keyword for "static class", but you can simulate it using:

✅ 1. Use Only @staticmethod Decorators
progarm:

class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Usage
print(MathUtils.add(3, 5))       # ✅ 8
print(MathUtils.subtract(10, 4)) # ✅ 6

You never create an object of MathUtils
All methods are bound to the class, not to any instance

✅2. PREVENT Instantiation (Optional):

You can prevent someone from creating an object of the class:

program:

class MathUtils:
    def __new__(cls):
        raise TypeError("This class cannot be instantiated")

    @staticmethod
    def add(x, y):
        return x + y

m = MathUtils()  # ❌ TypeError

✅3. ALTERNATIVE: Use a Module Instead of Static Class.
Python is a flexible language — if you're only using functions, you might not need a class at all.

program:

# math_utils.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
Then just import and use:

from math_utils import add

print(add(3, 5))

✅Summary:

Goal	How to Do It in Python
Static methods only	Use @staticmethod
Prevent instantiation	Override __new__ or __init__
Use functions without class	Just use a module with plain functions.