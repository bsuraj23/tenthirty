what are the difference between general method, normal method and abstract method?>
1. Normal Method (Regular Method)
Definition:
A method defined inside a class, usually with the self parameter, used to operate on object attributes.
Key Points:

Defined using def keyword.

Can be called using object of the class.

Fully implemented (i.e., it has code inside it).

Example:

python
Copy code
class Car:
    def start(self):
        print("Car started")
2. General Method
Note: "General method" is not an official Python term.
But people usually mean either a regular method (as above) or a standalone function (not in a class).

Interpretations:

1.Outside a class (like a utility function):


def add(x, y):
    return x + y
2.Inside class, but not special or abstract — same as normal method.

So, it’s just a general/regular method — no difference in functionality.

3. Abstract Method
Definition:
A method declared in an abstract class that does not have any implementation, and must be implemented in a child class.

Key Points:

Used in abstract base classes.

Created using the @abstractmethod decorator from abc module.

Enforces method overriding in subclasses.

Example:

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")
If Dog doesn’t implement sound(), it will give an error.