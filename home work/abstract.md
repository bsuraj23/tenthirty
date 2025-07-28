1. What is an Abstract Class?
An abstract class is a blueprint for other classes.
It cannot be instantiated (you can't create an object from it directly).

> Use:
To define common methods or structure for all child classes.

Force all subclasses to implement certain methods.

> How to define:
Use ABC (Abstract Base Class) from abc module.

2. What is an Abstract Method?
An abstract method is a method without a body (no code inside it).
It is declared in the abstract class, and all subclasses must implement it.

> Use:
Decorated with @abstractmethod.

Acts as a rule that child classes must follow.

 >When to Use?
When you have common functionality but want to force subclasses to complete some parts.

Example: Animal class has different sound() for each animal, but same sleep() method.

