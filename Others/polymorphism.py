class parent:
    def greet(self):
        print("Hello from parent to child")

class child:
    def greet(self):
        print("yes parent from child")

obj=child()
obj.greet()
obj=parent()
obj.greet()




class Dog:
    def sound(self):
        print("Barks🐕")
    def walk(self):
        print("walks🐕🚶‍♂️")
class cat:
    def sound(self):
        print("meows😺")
    def sleep(self):
        print("sleep🐈‍⬛")
obj=Dog()
obj.walk()
obj=cat()
obj.sleep()
