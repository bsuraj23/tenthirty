#34. How do you implement the Factory design pattern in Python?
# Step 1: Define the products
class Car:
    def drive(self):
        print("Driving a car")

class Bike:
    def drive(self):
        print("Riding a bike")

# Step 2: Create the factory
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")

# Step 3: Use the factory
vehicle1 = VehicleFactory.create_vehicle("car")
vehicle1.drive()   # Driving a car

vehicle2 = VehicleFactory.create_vehicle("bike")
vehicle2.drive()   # Riding a bike
