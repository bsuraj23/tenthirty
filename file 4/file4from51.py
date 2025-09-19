#Advanced Functional Programming:
# #51. What is a closure in Python? How is it different from a normal function?
#A closure in Python is a function that remembers variables from its outer function even after that function has finished.
#Example:
def outer(x):
    def inner(y):
        return x + y
    return inner
f = outer(5)
print(f(3))  # 8
#Difference from a normal function:
#Normal function: Doesn’t remember outer variables unless passed.
#Closure: Remembers variables from the outer function even after it’s done.
#52.Explain currying in Python with an example.
#What is Currying in Python?
#Currying is the process of transforming a function that takes multiple arguments into a sequence of functions, each taking a single argument.
#In Python, it means breaking down a function like f(x, y) into f(x)(y).
# Example:
def multiply(x):
    def inner(y):
        return x * y
    return inner
times3 = multiply(3)
print(times3(4))  # Output: 12
#55How do you implement functional pipelines in Python?
def add_one(x):
    return x + 1
def square(x):
 return x * x
def half(x):
    return x / 2
# Create a pipeline by applying functions one after another
def pipeline(x):
    return half(square(add_one(x)))
print(pipeline(3))  # Output: 8.0
#56.How do you implement tail recursion optimization (since Python doesn’t have it natively)?
def factorial(n):
    def helper(n, acc):
        if n == 0:
            return acc
        return helper(n-1, n * acc)
    return helper(n, 1)
print(factorial(5))  # Output: 120
#57. Explain higher-order functions with real-world use cases.
#Using map() to Process Data
prices = [100, 200, 300, 400]
def apply_discount(price):
    return price * 0.9  # 10% discount
discounted = list(map(apply_discount, prices))
print(discounted)  # [90.0, 180.0, 270.0, 360.0]
#59. How do you implement function composition in Python
def add2(x):
    return x + 2
def multiply3(x):
    return x * 3
# Compose functions: multiply3(add2(x))
result = multiply3(add2(4))  # (4 + 2) * 3 = 18
print(result)  # Output: 18
#60. What are monads in functional programming, and can they be represented in Python?
class Maybe:
    def __init__(self, value):
        self.value = value
    def bind(self, func):
        if self.value is None:
            return Maybe(None)
        return func(self.value)
    def __repr__(self):
        return f"Maybe({self.value})"
# Usage
result = Maybe(10).bind(lambda x: Maybe(x / 2)).bind(lambda x: Maybe(x + 3))
print(result)  # Maybe(8.0)
#81How do you implement your own context manager without using with?
#Implement a class with two methods
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

# Use it manually
ctx = MyContext()
ctx.__enter__()
print("Inside context")
ctx.__exit__(None, None, None)
#82. How do you implement your own decorator class with parameters?
#Create a class that’s callable (__call__) and accepts parameters in __init__.
#Example:
class Repeat:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper
@Repeat(3)
def greet():
    print("Hello!")
greet()  # Prints "Hello!" three times
#84. How do you implement operator overloading in Python?

#Define special methods like __add__, __str__, etc., in your class.

#Example:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__
print(p3.x, p3.y)  # 4 6

#85. How do you implement lazy evaluation in Python?
# Use generators or yield to produce values when needed, not in advance.
#Example:
def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
for number in lazy_range(5):
    print(number)  # Generates numbers one at a time



