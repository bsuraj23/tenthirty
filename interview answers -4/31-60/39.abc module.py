#39. How do abstract base classes (`abc` module) work in Python?
from abc import ABC, abstractmethod

# Define an abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Subclass implementing abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# This works
rect = Rectangle(4, 5)
print(rect.area())      # 20
print(rect.perimeter()) # 18

# This fails: cannot instantiate abstract class
# shape = Shape()  # TypeError


