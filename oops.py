#
# creat a class
class Car:
    def drive(self):
        print("The Car is moving")

# Create object
my_car = Car()
my_car.drive() 

# encapsulation   ;;;;
class Person:
    def __init__(self, name, age):
        self.__name = name   # private variable
        self.__age = age     # private variable

    def show(self):          # public 
        print("Name:", self.__name)
        print("Age:", self.__age)

p = Person("Sumanth", 23)
p.show()


# example 2
# Encapsulation Example
class Account:
    def __init__(self, name, balance):
        self.__name = name        # private variable
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_details(self):   # public 
        print("Name:", self.__name)
        print("Balance:", self.__balance)

acc = Account("Sumanth", 1000)
acc.deposit(500)
acc.show_details()



# abstraction
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):  # Abstract method (no body)
        pass

class Dog(Animal):   # Subclass
    def sound(self):
        print("Bark")

class Cat(Animal):   # Subclass
    def sound(self):
        print("Meow")

# Create objects
d = Dog()
d.sound()   # Output: Bark

c = Cat()
c.sound()   # Output: Meow

# example 2
# Abstraction Example
from abc import ABC, abstractmethod

class Device(ABC):  # Abstract class
    @abstractmethod
    def start(self):
        pass

class Laptop(Device):
    def start(self):
        print("Laptop is starting...")

class pc(Device):
    def start(self):
        print("Pc is booting...")

d1 = Laptop()
d2 = pc()

d1.start()
d2.start()



# inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d = Dog()
d.sound()

#example 2
class Animal:                   # Step 1: Parent class
    def eat(self):
        print("Animal eats food")

class Dog(Animal):              # Step 2: Child class inherits from Animal
    def bark(self):
        print("Dog barks")

# Step 3: Create object of child class
d = Dog()

# Step 4: Call both parent and child methods
d.eat()    
d.bark() 





#Polymorphism
class Bird:
    def fly(self):
        print("Some birds fly high")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

def show_flight(bird):
    bird.fly()

b1 = Bird()
p1 = Penguin()

show_flight(b1)
show_flight(p1)

# example 2
class Animal:                       # Step 1: Parent class
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):                 # Step 2: Child overrides method
    def speak(self):
        print("Dog barks")

class Cat(Animal):                # Step 2: Another child class
    def speak(self):
        print("Cat meows")

def make_sound(animal):            # Function accepts any object
    animal.speak()
make_sound(Dog())  
make_sound(Cat()) 




# different method
class student:
    student_name = "ABCD school"
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1= student("anil",34)
s2= student("sunil",56)

print("student 1 school:",s1.student_name,s1.name)
print("student 1 age:" ,s1.age,s1.name)
print("student 2 school:",s2.student_name,s2.name)
print("student 2 age:" ,s2.age,s2.name)






