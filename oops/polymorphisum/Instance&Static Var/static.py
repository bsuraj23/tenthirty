#Static variable are shared across all instances of a class
class Cars:
    wheels = 4  # Static variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
        
    def show(self):
        print(f"Car: {self.name}, Wheels: {Cars.wheels}")
        
c1 = Cars("Toyota")
c2 = Cars("Honda")

c1.show()  # Output: Car: Toyota, Wheels: 4
c2.show()  # Output: Car: Honda, Wheels: 4
