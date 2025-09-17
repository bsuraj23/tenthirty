#type() - it returns the exact type of an object
class Animal:
    pass
class Dog(Animal):
    pass
d=Dog()
print(type(d)==Dog)       #True
print(type(d)==Animal)   #false because it does not consider inheritance


