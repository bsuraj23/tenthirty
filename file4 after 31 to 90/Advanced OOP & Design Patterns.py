#Advanced OOP & Design Patterns
#31.Metaclasses in python
class AutoName(type):
    def __new__(mcls, name, bases, namespace):
        namespace.setdefault("auto_name", name.lower())
        return super().__new__(mcls, name, bases, namespace)

class MyClass(metaclass=AutoName):
    pass

print(MyClass.auto_name)
#32.Difference between type() and class in python
# runtime creation using type()
A = type("A", (), {"x": 1})
print(A, A.x)      
print(type(A))
#33.Create a singleton class in python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)
#34.Implement the factory design pattern in python
class Dog:
    def speak(self): return "woof"
class Cat:
    def speak(self): return "meow"

def animal_factory(kind):
    if kind == "dog": return Dog()
    if kind == "cat": return Cat()
    raise ValueError("unknown")

pet = animal_factory("dog")
print(pet.speak())
#35.Monkey patching in python
class Greeter:
    def greet(self): return "hi"

def excited_greet(self): return "HI!!!"

Greeter.greet = excited_greet 
g = Greeter()
print(g.greet())
#36.Implement mixins in python
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Base:
    def __init__(self, x): self.x = x

class MyThing(JsonMixin, Base):
    pass

t = MyThing(5)
print(t.to_json())
#37.Duck typing
class Duck:
    def quack(self): return "quack"

class Person:
    def quack(self): return "I can quack too"

def make_it_quack(thing):
    print(thing.quack())

make_it_quack(Duck())   
make_it_quack(Person())
#38.Multiple inheritance handled in python
class A: 
    def show(self): print("A")
class B(A):
    def show(self): print("B"); super().show()
class C(A):
    def show(self): print("C"); super().show()
class D(B, C):
    def show(self): print("D"); super().show()

d = D()
d.show()
print(D.__mro__)
#39.How abstract base classes work in python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.1416 * self.r * self.r

# Shape() -> TypeError
c = Circle(2)
print(c.area())
#40.Dependency injection in python
class Logger:
    def log(self, msg): print("LOG:", msg)

class Service:
    def __init__(self, logger):  
        self.logger = logger
    def do_work(self):
        self.logger.log("working")

# inject a real logger
svc = Service(Logger())
svc.do_work()

# inject a mock for testing
class MockLogger:
    def __init__(self): self.messages=[]
    def log(self, msg): self.messages.append(msg)

mock = MockLogger()
svc = Service(mock)
svc.do_work()
print(mock.messages)
