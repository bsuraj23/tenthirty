#Advanced Functional Programming
#What is a closure in Python? How is it different from a normal function?
# Closure: A closure is a function that "remembers" variables from its enclosing lexical scope, even after that scope has finished executing.
# Difference:
# A normal function only has access to its parameters and global variables.
# A closure captures and retains access to variables from its enclosing scope.
def outer(x):
    def inner(y):
        return x + y  
    return inner
add5 = outer(5)   
print(add5(10))   

#Explain currying in Python with an example.
# Currying: Transforming a function with multiple arguments into a sequence of single-argument functions.
# Python doesn’t support it natively but can be implemented with nested functions or functools.partial.
def multiply(x):
    def by(y):
        return x * y
    return by
double = multiply(2)
print(double(5))   

#What are partial functions (functools.partial)?
# A partial function fixes (or "freezes") some arguments of a function and returns a new function.
# Implemented using functools.partial.
from functools import partial
def power(base, exp):
    return base ** exp
square = partial(power, exp=2)
print(square(5))   

#What is memoization? How is it different from caching?
# Memoization: Storing results of expensive function calls based only on function inputs. Mostly used for recursion.
# Caching: A broader concept – storing results/data for reuse
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(40))  

#How do you implement functional pipelines in Python?
# A pipeline chains functions so the output of one is the input of the next.
def pipeline(data, funcs):
    for f in funcs:
        data = f(data)
    return data
result = pipeline(4, [lambda x: x+2, lambda x: x*3, lambda x: x-1])
print(result) 

#How do you implement tail recursion optimization (since Python doesn’t have it natively)?
# Python does not optimize tail recursion (stack frames are not reused).
# Workaround: Use a loop or decorator to simulate.
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
print(factorial(5))  

#Explain higher-order functions with real-world use cases.
# Higher-order function (HOF): A function that takes another function as argument or returns a function.
def logger(func):
    def wrapper(*args):
        print(f"Calling {func.__name__} with {args}")
        return func(*args)
    return wrapper
@logger
def add(a, b):
    return a + b
print(add(3, 4))   

#Difference between map/filter/reduce and comprehensions
# map/filter/reduce:
# Functional style, often less readable.
# map: applies a function to each element.
# filter: selects elements by condition.
# reduce: aggregates values.
# Comprehensions:
# More Pythonic, readable, supports inline expressions.
# Covers most cases of map and filter.
nums = [1,2,3,4,5]
squares = list(map(lambda x: x*x, nums))
squares2 = [x*x for x in nums]
evens = list(filter(lambda x: x%2==0, nums))
evens2 = [x for x in nums if x%2==0]

#How do you implement function composition in Python?
# Function composition: Combining two or more functions into one.
def compose(f, g):
    return lambda x: f(g(x))
def double(x): return x*2
def increment(x): return x+1
h = compose(double, increment)  
print(h(3))  

#What are monads in functional programming, and can they be represented in Python?
# Monad: A design pattern that represents computations as a series of steps
class Maybe:
    def __init__(self, value):
        self.value = value
    def bind(self, func):
        if self.value is None:
            return Maybe(None)
        return Maybe(func(self.value))
result = Maybe(5).bind(lambda x: x*2).bind(lambda x: None).bind(lambda x: x+10)
print(result.value)  

#Testing, Packaging & Deployment
#What is mocking in Python testing?
from unittest.mock import Mock
db = Mock()
db.get_user.return_value = {"id": 1, "name": "Alice"}
assert db.get_user(1)["name"] == "Alice"
