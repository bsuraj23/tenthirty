#52.Explain currying in Python with an example.
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)  # Fix a=2
triple = partial(multiply, 3)  # Fix a=3

print(double(5))  # 10
print(triple(5))  # 15
