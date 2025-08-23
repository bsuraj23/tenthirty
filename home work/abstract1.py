#normal/general method
class MyClass:
    def normal_method(self):
        print("This is a normal method")

obj = MyClass()
obj.normal_method()

# 2. Abstract Method

#example
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):
        pass  # No body

class Circle(Shape):
    def area(self):
        print("Area of circle is: π * r * r")

# shape = Shape()  
circle = Circle()   
circle.area()
