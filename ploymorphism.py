# example 1 overloading

class point:

    def __init__(self ,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
       return point(self.x +other .x, self.y + other.y)
    def __str__(self):
        return f"point({self.x}, {self.y})" 
p1=point(2,3)
p2=point(4,5)
sum_point = p1+p2
print("sum of point:", sum_point)

# example 2
#constructor overriding
class animal:
    def __init__(self, name):
        self.name = name
        print("animal constructor")
class dog(animal):        
    def __init__(self):
        print("dog constructor")    
d=dog()
a=animal("dog")

# example3
class Person:
    def __init__(self, name):
        self.name = name
        print("Person:", name)

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # Call Person's constructor
        self.grade = grade
        print("Student Grade:", grade)

s = Student("Ravi", "A")

# example 4
class shape:
    def __init__(self):
        print("shape of class")
class circle(shape):
    def __init__(self):
        super().__init__()
        print("circle of class")
class rectangle(shape):
    def __init__(self):
        
        print("rectangle of class")
def draw(shape):
    print("Drawing:",type(shape).__name__)
c=circle()
r=rectangle()    
draw(c)
draw(r)   

# overloading < and > operaters
class Box:
    def __init__(self, weight):
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

b1 = Box(50)
b2 = Box(30)

print(b1 > b2)  
print(b1 < b2)  

# function with different objects
class Car:
    def start(self):
        print("Car started")

class Bike:
    def start(self):
        print("Bike started")

def engine_start(vehicle):
    vehicle.start()

engine_start(Car())   
engine_start(Bike())  


#Polymorphism via Duck Typing
class Duck:
    def walk(self):
        print("Duck is walking")

class Person:
    def walk(self):
        print("Person is walking")

def walk_anything(obj):
    obj.walk()

walk_anything(Duck()) 
walk_anything(Person())  
