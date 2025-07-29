from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def speak(self):
        pass
class area(Shape):
    def speak(self):
        print("Dog barks")

a=area()
a.speak()
