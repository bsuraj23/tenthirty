#General/Normal method vs abstract method

#General/Normal methods that are defined in a class and have a proper implementation (i.e., body with code)
class Animal:
    def speak(self):
        print("The animal makes a sound")

a = Animal()
a.speak()

#Abstract method is a method without an implementation in the base class. It is meant to be overridden in child classes. 
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak() 


#Python does not have @abstractvariable or @abstractfunction. The only decorator is @abstractmethod

#Python function that takes a string and an integer to return the addition
def add_str_int(s, n):
    return int(s) + n
print(add_str_int("10",5))


#can you make entire class static?
#No, we cant make the entire class static but in python by using @staticmethod we can make methods static in a class

#Diff. b/w class and static method
#class method requires => class
#static method doesnt require a class or object