# Base class
class Vehicle:
    def __init__(self, brand, model):
        self._brand = brand            # Encapsulation: protected attribute
        self._model = model
    
    def display_info(self):
        print(f"Brand: {self._brand}, Model: {self._model}")

# Derived class (Inheritance)
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    # Polymorphism: Overriding method
    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}")

# Another derived class
class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity
    
    def display_info(self):
        super().display_info()
        print(f"Engine Capacity: {self.engine_capacity}cc")

# Creating objects
car1 = Car("Toyota", "Camry", 4)
bike1 = Motorcycle("Yamaha", "R15", 155)

# Demonstrating polymorphism
vehicles = [car1, bike1]
for v in vehicles:
    v.display_info()
    print("---")
