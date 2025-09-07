# Basic Class and Object

class Student:
    def display(self):
        print("This is a Student class.")

# Create object
s = Student()
s.display()

# Class with Constructor (__init__)

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

# Create object with constructor
p = Person("Archana")
p.greet()

# Class with Multiple Attributes

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Create object and call method
r = Rectangle(10, 5)
print("Area:", r.area())

# Class with Multiple Methods

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

c = Calculator()
print("Sum:", c.add(3, 5))
print("Product:", c.multiply(4, 6))

# Class with User Input

class Student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.marks = int(input("Enter marks: "))

    def show(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s = Student()
s.show()
