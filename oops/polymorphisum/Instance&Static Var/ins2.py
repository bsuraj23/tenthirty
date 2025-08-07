#usind __dict__ to print instance variables
class car:
    def __init__(self, brand, model):
        self.brand = brand          # Instance variable
        self.model = model          # Instance variable
car1 = car("BENZ", "G-Vagon")
car2 = car("Honda", "Civic")

print(car1.__dict__)
print(car2.__dict__)