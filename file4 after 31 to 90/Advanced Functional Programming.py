#Advanced Functional Programming
#51.Closure
def outer(x):
    def inner(y):
        return x + y 
    return inner

add5 = outer(5)
print(add5(10))
#52.Currying
def multiply(x):
    def by(y):
        return x * y
    return by

double = multiply(2)
print(double(5))
#53.Partial functions
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print(square(5))
#54.Memoization vs Caching
from functools import lru_cache

@lru_cache(maxsize=None)   
def fib(n):
    if n<2: return n
    return fib(n-1)+fib(n-2)

print(fib(30))
#55.Functional pipelines
def pipeline(data, *funcs):
    for f in funcs:
        data = f(data)
    return data

# Example pipeline
def add1(x): return x+1
def times2(x): return x*2

print(pipeline(3, add1, times2))
#56.Tail recursion
def factorial(n):
    result = 1
    while n>1:
        result *= n
        n -= 1
    return result

print(factorial(5))
#57.Higher order functions
def apply_twice(func, x):
    return func(func(x))

print(apply_twice(lambda x:x+1, 3))
#58.Map/filter/reduce vs comprehensions
nums=[1,2,3]
print(list(map(lambda x:x*2, nums)))
print([x*2 for x in nums])
#59.Function composition
def compose(f,g):
    return lambda x: f(g(x))

def double(x): return x*2
def add1(x): return x+1

h = compose(double, add1) 
print(h(3))
#For multiple functions:

from functools import reduce
def compose_many(*funcs):
    return reduce(lambda f,g: lambda x: f(g(x)), funcs)
#60.Monads
class Maybe:
    def __init__(self, value):
        self.value = value
    def bind(self, func):
        if self.value is None:
            return self  
        return func(self.value)

# Usage:
result = Maybe(5).bind(lambda x: Maybe(x*2)).bind(lambda x: Maybe(x+3))
print(result.value)