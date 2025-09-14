#inheritance
class Animal:  # Parent class
    def speak(self):
        return "I make sounds"

class Dog(Animal):  # Child class inherits Animal
    def speak(self):   # Overriding
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!

#Polymorphism
animals = [Dog(), Cat()]
for animal in animals:     #here Both Dog and Cat use the same method speak(), but output differs.
    print(animal.speak())  # Dog → Woof!, Cat → Meow!   

#Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
# print(acc.__balance) it shows AttributeError

#Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract class
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine started"

class Bike(Vehicle):
    def start(self):
        return "Bike engine started"

car = Car()
bike = Bike()
print(car.start())  # Car engine started
print(bike.start()) # Bike engine started
#we cannot instantiate Vehicle class directly, only its child classes that implement start().