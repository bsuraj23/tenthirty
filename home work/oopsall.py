
# Multiple Objects of a Class

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "car started")

# Create objects
car1 = Car("Honda")
car2 = Car("Hyundai")

car1.start()
car2.start()

 #Class with Inheritance 

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

#Example: Single Inheritance

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()  # From parent
d.bark()   # From child
#Example: Multi-level Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

p = Puppy()
p.eat()
p.bark()
p.weep()

#Example: Multiple Inheritance

class Father:
    def home(self):
        print("Father's home")

class Mother:
    def jewelry(self):
        print("Mother's jewelry")

class Child(Father, Mother):
    def toys(self):
        print("Child's toys")

c = Child()
c.home()
c.jewelry()
c.toys()

# Example: Polymorphism with Functions and Classes

class Cat:
    def sound(self):
        print("Cat meows")

class Dog:
    def sound(self):
        print("Dog barks")

# Same method name, different classes
def animal_sound(animal):
    animal.sound()

c = Cat()
d = Dog()

animal_sound(c)
animal_sound(d)

#Example: Method Overriding (Polymorphism through Inheritance)

class Vehicle:
    def start(self):
        print("Vehicle starting...")

class Car(Vehicle):
    def start(self):  # Overriding parent method
        print("Car starting...")

v = Vehicle()
v.start()

c = Car()
c.start()

 #1. Simple Encapsulation using Private Variable

class Student:
    def __init__(self):
        self.__name = "Archana"  # private variable

    def show_name(self):
        print("Name is:", self.__name)

s = Student()
s.show_name()

# Encapsulation with Getter and Setter

class Student:
    def __init__(self):
        self.__marks = 0  # private variable

    def set_marks(self, m):
        self.__marks = m

    def get_marks(self):
        print("Marks:", self.__marks)

s = Student()
s.set_marks(90)
s.get_marks()
