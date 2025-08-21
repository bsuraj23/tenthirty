class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print(f"{self.brand},{self.model} is my car")
    def sound(self):
        print("VROOM!")

class EV(Car):
    def sound(self):
        print("It makes no sound")

car1=Car("BenZ","G-Vagon")
car2=EV("Tesla","CyberTruck")

car1.display()
car2.display()