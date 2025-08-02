#single inheritence
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()
d.bark()

#multiple inheritence
class Father:
    def work(self):
        print("Father goes to office")

class Mother:
    def cook(self):
        print("Mother cooks food")

class Child(Father, Mother):
    def play(self):
        print("Child plays games")

c = Child()
c.work()
c.cook()
c.play()

#multilevel inheritence
class Grandparent:
    def house(self):
        print("Grandparent has a house")

class Parent(Grandparent):
    def car(self):
        print("Parent has a car")

class Child(Parent):
    def bike(self):
        print("Child has a bike")

ch = Child()
ch.house()
ch.car()
ch.bike()

#hierarchical inheritence
class Parent:
    def property(self):
        print("Parent has property")

class Child1(Parent):
    def job(self):
        print("Child1 has a job")

class Child2(Parent):
    def business(self):
        print("Child2 runs a business")

c1 = Child1()
c2 = Child2()

c1.property()
c1.job()

c2.property()
c2.business()

#hybrid inheritence
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C:
    def showC(self):
        print("Class C")

class D(B, C):
    def showD(self):
        print("Class D")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()
