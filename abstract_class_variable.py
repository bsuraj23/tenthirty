#An abstract class is a class that cannot be instantiated directly. It may contain:
#Abstract methods (methods without a body)
#Abstract variables (properties that must be overridden)
#Normal methods and variables too

#An abstract variable is a class-level attribute that must be defined in child classes. Python doesn’t support it directly like methods, but we can use a trick using @property and @abstractmethod.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self):
        pass  # Abstract variable

    @abstractmethod
    def start(self):
        pass  # Abstract method

# Child class must implement both
class Bike(Vehicle):
    @property
    def wheels(self):
        return 2

    def start(self):
        print("Bike started with kick")

# Create object
b = Bike()
print("Wheels:", b.wheels)
b.start()
