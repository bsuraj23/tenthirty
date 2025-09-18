#OOP in Python
#Create a class BankAccount with methods deposit, withdraw, and check_balance
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

account = BankAccount()
account.deposit(1000)
account.withdraw(500)
account.check_balance()

#Implement inheritance with a base class Shape and derived classes Circle and Rectangle with an area() method
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())

#Implement a class with a static method to check if a number is even
class MathUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

print(MathUtils.is_even(10))  
print(MathUtils.is_even(7))   

#Create a class Car that tracks the number of cars created using a class variable
class Car:
    car_count = 0 

    def __init__(self, model):
        self.model = model
        Car.car_count += 1

    def display(self):
        print(f"Car model: {self.model}")

car1 = Car("Toyota")
car2 = Car("Honda")
car3 = Car("Ford")

print("Total cars created:", Car.car_count)

#Override the __str__ method in a class to display custom output
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

p = Person("Alice", 25)
print(p)  
