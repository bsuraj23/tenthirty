#OOP in python
#21.Bank account
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance           

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:         
            self.balance -= amt

    def check_balance(self):
        return self.balance
acc=BankAccount(10000)
acc.deposit(5000)
acc.withdraw(2000)
print(acc.check_balance())
#22.Inheritance
class Shape:
    pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):   
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
c = Circle(5)
r = Rectangle(4, 6)
print("Circle area:", c.area())
print("Rectangle area:", r.area())
#23.Static method
class Utils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
print(Utils.is_even(4))
print(Utils.is_even(7))
#24.Class variable count
class Car:
    count = 0                

    def __init__(self):
        Car.count += 1
c1 = Car()
c2 = Car()
c3 = Car()
print("Cars created:", Car.count)
#25.__str__ method
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"
p = Person("Sindhuja")
print(p)  