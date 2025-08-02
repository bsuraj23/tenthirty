#Difference between general/normal method and Abstract method

✅ 1. Normal Method / General Method
In most contexts, "normal method" and "general method" mean the same thing — a regular method defined inside a class using def, which can be called using an object of that class.

🔹 Example:

class MyClass:
    def greet(self):
        print("Hello from normal/general method!")

obj = MyClass()
obj.greet()
✔️ This is a fully defined method that:

Has a body

Is directly callable

Is not abstract

✅ 2. Abstract Method
An abstract method is a method that is declared but not implemented in the base class. It forces child classes to override and implement the method.

To define an abstract method, you use:

from abc import ABC, abstractmethod

Make the class inherit from ABC (Abstract Base Class)

🔹 Example:

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark!")

# a = Animal()  # ❌ Error: Can't instantiate abstract class
d = Dog()
d.sound()
✔️ Abstract methods:

Have no implementation in the base class

Must be implemented by derived classes

Make the class abstract, so it can't be instantiated

