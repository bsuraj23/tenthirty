What is Abstract Class:
A class that cannot be instantiated directly.

Contains abstract methods (methods without body).

Created using ABC (Abstract Base Class) and @abstractmethod.

Used to define a common interface for child classes.

#Example

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

What is Abstract Variable:
Python doesn't support abstract variables directly.

You can simulate using @property + @abstractmethod.

Forces child class to define a specific property.

#Example

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass
