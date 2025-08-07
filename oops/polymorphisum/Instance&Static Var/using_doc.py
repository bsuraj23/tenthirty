#It prints whathever in this """    """ three characters
class Car:
    """This is a Car class that represents a car with a brand and model."""
    def __init__(self, Brand, Model):
        self.brand = Brand          # Instance variable
        self.model = Model          # Instance variable
        
car1= Car("BENZ", "G-Vagon")
car2= Car("Honda", "Civic")

print(Car.__doc__)
print(car1.__dict__)
print(car2.__dict__) 