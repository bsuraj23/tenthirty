class car:
        @staticmethod
        def start():
            print("Car started.")
        
        @staticmethod
        def stop():
            print("Car stopped.")

class bmw(car):
     def __init__(self, name):
            self.name = name

car1 = bmw("BMW X5")
# car2 = bmw("BMW M2")

print(car1.start())         
          

