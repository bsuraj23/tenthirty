#Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Create object
d = Dog()
d.speak()
d.bark()

#Multilevel Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Create object
p = Puppy()
p.speak()
p.bark()
p.weep()

#Multiple Inheritance
class Father:
    def skills(self):
        print("Gardening and Programming")

class Mother:
    def skills(self):
        print("Cooking and Art")

class Child(Father, Mother):
    def show(self):
        print("Child has following skills:")

# Create object
c = Child()
c.show()
c.skills()

#Encapsulation
class Person:
    def __init__(self, name):
        self.__name = name  # private variable

    def get_name(self):
        return self.__name  # public method to access private variable

    def set_name(self, name):
        self.__name = name  # public method to modify private variable

# Create object
p = Person("John")

# Access name using getter
print("Name:", p.get_name())

# Modify name using setter
p.set_name("Alice")
print("Updated Name:", p.get_name())

#Polymorphism
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

# Function showing polymorphism
def animal_sound(animal):
    animal.sound()

# Create objects
d = Dog()
c = Cat()

# Call the function with different objects
animal_sound(d)
animal_sound(c)
