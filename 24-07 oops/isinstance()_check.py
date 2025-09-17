#isinstance-checks if an object is an instance of a class or its subclasses
class Animal:
    pass
class Dog(Animal):
    pass
d=Dog()
print(isinstance(d,Dog))  #True 
print(isinstance(d,Animal)) #True - because it supports inheritance

