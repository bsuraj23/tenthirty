| Method Type         | Defined In                   | Has Body?           | Must Be Overridden? | Can Be Called Directly?    | Purpose                                 |
| ------------------- | ---------------------------- | ------------------- | ------------------- | -------------------------- | --------------------------------------- |
| **General Method**  | Any class (often base)       | ✅ Yes               | ❌ No                | ✅ Yes                      | Regular function inside a class         |
| **Normal Method**   | Synonym for general          | ✅ Yes               | ❌ No                | ✅ Yes                      | Same as general method                  |
| **Abstract Method** | Abstract class (using `abc`) | 🚫 No (only `pass`) |  ✅ Yes (in subclass) | ❌ No (must override first) | Forces subclass to implement the method |

1. GENERAL / NORMAL Method
These are just regular instance methods with a body, defined in any class (base or child). "General" and "normal" are often used interchangeably.

program:

class Animal:
    def speak(self):
        print("Animal speaks")

a = Animal()
a.speak()                   # ✅ Output: Animal speaks.

You can call them directly.
You can override them, but it's not required.

2. ABSTRACT Method
Defined in an abstract base class using @abstractmethod. It acts as a placeholder: child classes must implement it.

program:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bark")

# a = Animal()  # ❌ Error: Can't instantiate abstract class
d = Dog()
d.speak()        # ✅ Output: Bark

Can't have a complete body (usually just pass)
Forces subclasses to define that method.
Abstract classes cannot be instantiated.