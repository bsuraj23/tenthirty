class car:
        def __init__(self, type):
              self.type = type

        @staticmethod
        def start():
            print("Car started.")
        
        @staticmethod
        def stop():
            print("Car stopped.")


class Bmw(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = Bmw("X5", "electric")
# car2 = bmw("BMW M2")

print(car1.type)

          
