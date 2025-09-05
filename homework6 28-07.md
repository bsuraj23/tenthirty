#How can you make a class as a static

In Python, you cannot make an entire class "static" like in some other languages such as Java. However, you can achieve similar behavior by:

Using a class with only @staticmethods and class-level variables
This simulates a "static class" — a class that is never instantiated, and all its methods and variables are accessed directly from the class.

Example: Static-like Class in Python

class MathUtils:
    PI = 3.14159

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def area_of_circle(radius):
        return MathUtils.PI * radius * radius
Usage:
print(MathUtils.add(5, 3))          
print(MathUtils.area_of_circle(2))   
