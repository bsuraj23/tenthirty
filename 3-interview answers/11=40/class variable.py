#Create a class `Car` that tracks the number of cars created using a **class variable**.
class Car:
    # Class variable to track number of cars
    car_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count += 1   # increment when a new car is created

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

    @classmethod
    def total_cars(cls):
        return cls.car_count


# Example usage
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Tesla", "Model 3")

car1.display_info()
car2.display_info()
car3.display_info()

print("Total cars created:", Car.total_cars())
