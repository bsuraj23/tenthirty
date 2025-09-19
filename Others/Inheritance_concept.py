# parent class Parent:
# Example:1 
class Animal:
        def speak(self):
            print("Animal makes sounds")

class cat(Animal):
    def speak( sekf):
        print("Speak meow")

c = cat()
c.speak()


# Example:2
# Single Inheritance

class vehicle:
    def info(self):
        print("This is a vehicle")

class car(vehicle):
    def brand(self):
        print("Car brand is Thar")

class bike(vehicle):
    def brand(self):
        print("Bike brand is Royal Enfield")       

c = car()
c.info()
c.brand()
b = bike()
b.info()
b.brand()

# Example:3
# Multilevel Inheritance

class GrandParent:
    def greet(self):    
        print("Hello from GrandParent")


class Parent(GrandParent):
    def Hello (self):
       print("Hello from Parent")

class Child(Parent):
    def Hello(self):
        print("Hello from clild")

c = Child()
c.greet()  # Inherited from GrandParent
c = Child()
c.Hello()  # Overridden in Child
c = Parent()
c.Hello()  # Inherited from Parent

# Example:4
# Multiple Inheritance

class Father:
    def skill(self):
        print("Father's skill: Driving")

class Mother:
    def talent(self):
        print("Mother's talent: Cooking")

class Child(Father, Mother):  
    def hobby(self):
        print("Child's hobby: Painting")

c = Child()
c.skill()
c.talent()
c.hobby()


#  Example 5: Real-Time Example

class Employee:
    def __init__(self, name,salary):
        self.name = ("Mr.SUnil")
        self.salary = (35000)

    def show (self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  
        self.department = department

    def show(self):
        super().show()  
        print(f"Department: {self.department}")  
        
    def show_manager(self):
        print(f"Manager: {self.name}, Dept: {self.department}, Salary: {self.salary}")

m = Manager("Mr.Sunil", 35000, "IT")
m.show()
m.show_manager()












