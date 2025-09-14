#Inheritance (Shape - Circle, Rectangle)
import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def are(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.lenght * self.width
    
circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())


#Class Variable to track Cars
class Car:
    total_cars = 0 

    def __init__(self,brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars
    
c1 = Car("Tesla")
c2 = Car("BMW")
print("Total cars created:", Car.get_total_cars())

#static method to check even number
class NumberUtils:
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
print(NumberUtils.is_even(4))
print(NumberUtils.is_even(5))