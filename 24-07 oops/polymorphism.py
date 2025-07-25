class Bird:
    def fly(self):
        print("Birds flies in the sky")
class Airplane:
    def fly(self):
        print("Airplanes flies in the air")

def flying_test(obj):
    obj.fly()

flying_test(Bird())
flying_test(Airplane())