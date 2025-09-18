#59.How do you implement function composition in Python?

from functools import reduce

def compose(*funcs):
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

def double(x): return x * 2
def increment(x): return x + 1
def square(x): return x ** 2

pipeline = compose(square, increment, double)
print(pipeline(3))  # square(increment(double(3))) → 49
