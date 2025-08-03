class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model
    def sound(self):
        print("This car makes sound,Vroom Vroom!")
    def display(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")
        
class EV(Car):
        def sound(self):
            print("Electric cars are quiet!")
            
car1=Car("Benz","G-Vagon")
car1.display()
car1.sound()

car2=EV("Tesla","Model S")
car2.display()
car2.sound()


