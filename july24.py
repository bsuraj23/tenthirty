# pdb.set_trace()

# pdb.set_trace()` is a **built-in Python function** that **activates the debugger** 
# at the point in your code where it's called.


# # What It Does :

# 1. **Pauses** execution of the program.
# 2. **Enters interactive debugging mode** in the terminal or console.

# Syntax :
# import pdb
# pdb.set_trace()

#  Example

# def greet(name):
#     import pdb; pdb.set_trace()
#     message = f"Hello, {name}"
#     print(message)

# greet("Alice")

# When run, you’ll see something like:

# > test.py(3)greet()
# -> message = f"Hello, {name}"
# (Pdb)

# Now you can enter debugger commands at (Pdb), such as:

# * `p name` → prints `"Alice"`
# * `n` → next line
# * `q` → quit


## OOPS
# Object-Oriented Programming (OOP) is a programming paradigm
#  that structures code using classes and objects.

# Instead of writing code with just functions and variables, 
# OOP helps you model real-world things (like cars, users, bank accounts)
#  as objects with properties (attributes) and behaviors (methods).

# Four Main OOP Concepts in Python
# 1. Class and Object
# A class is a blueprint for creating objects.

# An object is an instance of a class.

class Dog:
    def __init__(self, name):     # Constructor
        self.name = name          # Attribute

    def bark(self):               # Method
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")             # Object creation
my_dog.bark()                     # Output: Buddy says Woof!

# 2. Encapsulation
# Hides internal state and behavior.

# Keeps data safe from outside interference.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acct = BankAccount(1000)
acct.deposit(500)
print(acct.get_balance())          # Output: 1500
# print(acct.__balance) → Error! It's private.

# 3. Inheritance
# A class can inherit properties and methods from another class.

class Animal:
    def speak(self):
        print("Some generic sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

my_cat = Cat()
my_cat.speak()                     # Output: Meow

# Polymorphism
# Same method name behaves differently depending on the object.

class Bird:
    def sound(self):
        print("Tweet")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

make_sound(Bird())                # Output: Tweet
make_sound(Dog())                # Output: Bark


# __init__() and self :
# __init__() is a constructor—runs when you create an object.

# self refers to the current instance (like this in other languages).

# | Concept           | Purpose                               |
# | ----------------- | ------------------------------------- |
# | **Class**         | Blueprint/template for objects        |
# | **Object**        | Instance of a class                   |
# | **Encapsulation** | Protects data using private variables |
# | **Inheritance**   | Enables code reuse between classes    |
# | **Polymorphism**  | Allows methods to behave differently  |

