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