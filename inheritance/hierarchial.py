#example1
# Parent class
class Animal:
    def sound(self):
        print("Animals make sound")

# Child class 1
class Dog(Animal):
    def breed(self):
        print("Breed: Labrador")

# Child class 2
class Cat(Animal):
    def color(self):
        print("Color: White")

# Child class 3
class Cow(Animal):
    def gives(self):
        print("Gives: Milk")

# Creating objects
d = Dog()
d.sound()
d.breed()

c = Cat()
c.sound()
c.color()

co = Cow()
co.sound()
co.gives()

#example2
class Person:
    def details(self):
        print("Name and age")

class Student(Person):
    def role(self):
        print("I am a Student")

class Teacher(Person):
    def role(self):
        print("I am a Teacher")

class Principal(Person):
    def role(self):
        print("I am a Principal")

s = Student()
s.details()
s.role()

t = Teacher()
t.details()
t.role()

p = Principal()
p.details()
p.role()