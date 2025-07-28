#Normal Method
class Animal:
    def speak(self):
        print("Animal makes a sound")

a = Animal()
a.speak()

#General Method
class Utility():
    def instance_method(self):
        print("Instance method")
    @classmethod
    def class_method(cls):
        print("Class method")
    @staticmethod
    def static_method():
            print("Static method")
u = Utility()
u.instance_method()
Utility.class_method()
Utility.static_method()

#abstract method
from abc import ABC, abstractmethod
class shape(ABC):
     @abstractmethod
     def area(self):
          pass
     
class circle(shape):
     def area(self):
          print("Area of the circle")

c = circle()
c.area()               