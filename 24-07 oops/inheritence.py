class Animal:
    def sound(self):
        print("Animal can make sound")
class Dog(Animal):
    pass
        
d=Dog()
d.sound()
    
class Parent:
    def display(self):
        print("Parent class")
class Child(Parent):
    def display(self):
        
        print("Child class")
pobj=Parent()
cobj=Child()

pobj.display()
cobj.display()
