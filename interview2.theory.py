🔹 Decorators & Context Managers

41. What are decorators in Python?
A decorator is a function that takes another function (or class) as input, extends or modifies its behavior, and returns it.
They are written using the @decorator_name syntax.
Example:

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()


42. Can a function return another function in Python?
Yes ✅, functions are first-class objects in Python.

def outer():
    def inner():
        return "Inner function"
    return inner

f = outer()
print(f())   # "Inner function"


43. What is a higher-order function?
A function that either:

takes another function as an argument, OR

returns another function.

Examples: map(), filter(), sorted(key=...).

44. What is a context manager in Python?
It manages resources (like files, DB connections) automatically using with.
Example:

with open("file.txt", "r") as f:
    data = f.read()

45. What is the difference between with and try-finally?

try-finally: you manually ensure cleanup in finally.

with: cleanup is automatic using context manager’s __enter__ and __exit__ methods.
with is cleaner and less error-prone.

🔹 Modules & Imports

46. What is the difference between a module and a package?

Module → A single .py file (e.g., math.py).

Package → A directory containing multiple modules + an __init__.py file.

47. What does __name__ == "__main__" mean in Python?
When a Python file is run directly, __name__ == "__main__" is True.
When imported as a module, __name__ is the module name.
Used to control code execution.

48. What is the difference between import and from-import?

import math
print(math.sqrt(9))   # access with module name

from math import sqrt
print(sqrt(9))        # directly use function


49. How do relative imports work in Python?
Relative imports use . notation:

from . import moduleA (current package)

from .. import moduleB (parent package)
Used within packages.

50. How does Python search for modules when importing?
It checks:

Current directory

PYTHONPATH environment variable

Standard library

site-packages (installed packages)

🔹 Namespaces & Scope

51. What is the LEGB rule in Python?
Order Python looks for variables:

L → Local

E → Enclosing (in nested functions)

G → Global (module-level)

B → Built-in (Python keywords/functions)

52. What is the difference between global and local variables?

Local → defined inside a function, accessible only there.

Global → defined outside functions, accessible everywhere.

53. How do you use the global keyword in Python?
To modify a global variable inside a function:

x = 5
def update():
    global x
    x = 10


54. How do you use the nonlocal keyword?
Used in nested functions to modify variables in enclosing (non-global) scope:

def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)  # 10


55. What happens when two variables with the same name exist in different scopes?
Python uses the closest scope according to LEGB rule.
Local > Enclosing > Global > Built-in.

🔹 Data Handling

56. How do you read and write files in Python?

with open("data.txt", "w") as f:
    f.write("Hello")

with open("data.txt", "r") as f:
    print(f.read())


57. What is the difference between text mode and binary mode in file handling?

Text mode ("r", "w") → Reads/writes strings.

Binary mode ("rb", "wb") → Reads/writes raw bytes (images, videos).

58. How do you handle CSV files in Python?

import csv

# Writing
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])

# Reading
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


60. How do you handle command-line arguments in Python?
Using argparse:

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")
args = parser.parse_args()

print("Hello", args.name)

🔹 Functional Programming

61. What is the difference between map(), filter(), and reduce()?

map(func, iterable) → applies function to each element.

filter(func, iterable) → keeps elements where func returns True.

reduce(func, iterable) → reduces iterable to a single value.

62. What is a lambda function?
An anonymous (inline) function defined with lambda.

square = lambda x: x ** 2
print(square(5))  # 25


63. Can you give an example where filter() is useful?

numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4]


64. How does reduce() work in Python?

from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)   # 10


It applies the function cumulatively.

65. What is the difference between list comprehension and map()?

List comprehension → More Pythonic, readable, can include conditions.

map() → Functional, applies only one function to all elements.

Example:

# list comprehension
squares1 = [x**2 for x in range(5)]

# map
squares2 = list(map(lambda x: x**2, range(5)))