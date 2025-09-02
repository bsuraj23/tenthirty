# normal method
class car():
    def drive(self):
        print("iam driving car")
c=car()
c.drive()

# general method
class calculator():
    def add(self,a,b):
        return a+b
c=calculator()
print(c.add(5,3))  

# abstract method
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def sound(self):  # Abstract method
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create objects
d = Dog()
d.sound()

c = Cat()
c.sound()
