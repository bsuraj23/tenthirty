#class and object with encapsulation
# Class definition
class Student:
    def __init__(self, name, grade):
        self.name = name        # public attribute
        self.__grade = grade    # private attribute (encapsulation)

    def display(self):
        print("Name:", self.name)
        print("Grade:", self.__grade)

# Creating object
s1 = Student("Alice", "A")
s1.display()

#inheritence
# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Creating objects
a = Animal()
d = Dog()

a.speak()
d.speak()

#polymorphism
class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Polymorphism
shapes = [Square(4), Circle(3)]

for shape in shapes:
    print("Area:", shape.area())
