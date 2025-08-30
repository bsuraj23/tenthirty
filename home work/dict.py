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