#Implement inheritance with a base class `Shape` and derived classes `Circle` and `Rectangle` with an `area()` method.
import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Example usage
shapes = [
    Circle(5),
    Rectangle(4, 6)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
