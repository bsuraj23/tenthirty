# example super() with parameters
class Person:
    def __init__(self, name,age):
        self.name = name
        print("Person name:", name)
        self.age = age
        print("person age:", age)

class Student(Person):
    def __init__(self, name, grade,age):
        super().__init__(name,age)     # 👈 Calls parent constructor
        self.grade = grade
        print("Student grade:", grade)
        self.age = age
        print("student age:", age)

s = Student("Anil", "A",23)

# example 1  Using super() to call parent constructor

class Parent:
    def __init__(self):
        print("Parent constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()   # Call parent constructor
        print("Child constructor called")

c = Child()


# example 2  Using super() to call parent method


class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call parent method
        print("Dog barks")

d = Dog()
d.speak()

