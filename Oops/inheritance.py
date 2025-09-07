class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def display_info(self):
        print("My car brand is", self.brand, "and model is", self.model)
    def fueltype(self):
        print("diesel")

class EV(Car):
    def fueltype(self):
        print("It doesnot require fuel")

car1=Car("Toyota", "Fortuner")
car2=Car("Bmw", "M5")
car3=Car("Tesla", "modelx")
    
car1.display_info()
car2.display_info()
car3.display_info()

