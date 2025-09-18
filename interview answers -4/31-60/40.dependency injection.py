#40.Explain dependency injection in Python with an example.
class Engine:
    def start(self):
        print("Engine started")

class ElectricEngine:
    def start(self):
        print("Electric engine started")

class Car:
    def __init__(self, engine):  # inject dependency
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("Car is driving")

# Inject dependency from outside
engine = Engine()
car1 = Car(engine)
car1.drive()
# Output:
# Engine started
# Car is driving

# Inject a different dependency
electric_engine = ElectricEngine()
car2 = Car(electric_engine)
car2.drive()
# Output:
# Electric engine started
# Car is driving
