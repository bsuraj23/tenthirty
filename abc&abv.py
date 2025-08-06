1. AbSTRACT CLASS
An abstract class is a class that cannot be instantiated and is meant to be subclassed.

It can contain:
Abstract methods (which must be implemented by child classes)
Concrete methods (with actual code)
Abstract properties or variables.
example :

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass
Abstract class : Base class that defines structure but can't be instantiated.

2. ABSTRACT VARIABLE (or Abstract Property)
An abstract variable (also called an abstract property) is a placeholder for a property that must be defined in child classfrom abc import ABC, abstractpropertyes.

example

class MyAbstractClass(ABC):
    @property
    @abstractmethod
    def name(self):
        pass


Abstract variable/property:  Enforces that subclasses define specific attributes or computed properties.


| Feature                  |     Abstract Class                                |   Abstract Variable (Property)                  |
| ------------------------ | ---------------------------------------- | --------------------------------------------- |
| **Purpose**              |    To define a base class with common API   |        To enforce the definition of a property       |
| **Defined using**        |    `class MyClass(ABC)`                     | `           @property` + `@abstractmethod`               |
| **Can contain methods?** |    Yes (abstract or concrete)               |        No — variables only                           |
| **Can be instantiated?** |    ❌ No (must be subclassed)                |      ❌ Cannot be skipped in subclass               |
| **Enforces**             |     Implementation of abstract methods/props |       Presence of specific attributes in subclasses |
