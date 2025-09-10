 # Parent class
class Animal:
    def eat(self):
        print("I can eat")

# Child class
class Dog(Animal):
    def bark(self):
        print("I can bark")

# Usage
d = Dog()
d.eat()
d.bark()
