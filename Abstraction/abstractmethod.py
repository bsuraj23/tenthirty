from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car Engine Started"
    def stop(self):
        return "Car Engine Stopped"
    
class Bike(Vehicle):
    def start(self):
        return "Bike Engine Started"
    def stop(self):
        return "Bike Engine Stopped"
    
v1=Car()
v2=Bike()


print(v1.start())
print(v1.stop())
print(v2.start())
print(v2.stop())