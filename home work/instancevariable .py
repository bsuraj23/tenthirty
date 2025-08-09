#Python Program for Instance Variable:
class Car:
    def __init__(self, brand, model):
        # Instance variables
        self.brand = brand
        self.model = model

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Creating objects (instances)
car1 = Car("Toyota", "Fortuner")
car2 = Car("Hyundai", "Creta")

# Accessing instance variables
car1.show_details()
print("-----")
car2.show_details()

#Simple __dict__ Program:

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# Create an object
s1 = Student("Archu", 468)

# Print instance variables using __dict__
print(s1.__dict__)
