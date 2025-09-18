#Modules & Imports
#41.Two modules (module1.py & module2.py)
# module1.py
def greet(name):
    return f"Hello, {name}!"
# module2.py
import module1          
print(module1.greet("Sindhu"))
#42.is_palindrome() helper in a module
# helpers.py
def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]
#test_palindrome.py
import helpers
print(helpers.is_palindrome("Racecar"))
print(helpers.is_palindrome("Hello"))
#43.__name__ == "__main__"
def say_hi():
    print("Hi!")
if __name__ == "__main__":
    say_hi()
#44.Package with __init__.py and relative imports
mypkg/
__init__.py
a.py
b.py
mypkg/a.py
def fun_a():
    return "function a result"
mypkg/b.py
from .a import fun_a 
def fun_b():
    return "b uses -> " + fun_a()
test_pkg.py
import mypkg.b
print(mypkg.b.fun_b())
#45.math module demo
import math

print(math.sqrt(16))
print(math.sin(0))
print(math.factorial(5))