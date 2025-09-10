class Animal:
    def speak(self):
       print("The animal makes sound")
class Dog(Animal):
    def bark(self):
        print("The dog barks")
d=Dog()
d.speak()
d.bark()

#using constructor
#parent class
class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def show(self):
        self.display()
        print("roll number:",self.roll)
s=student("Sindhuja",1)
s.show()

#Adding more methods in child
class vehicle:
    def start(self):
        print("The vehicle started")
class car(vehicle):
    def drive(self):
        print("car is being driven")
c=car()
c.start()
c.drive()
