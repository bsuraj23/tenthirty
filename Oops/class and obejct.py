class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def greet(self):
        print ("Hello, my name is", self.name, "and I am", self.age, "years old")

p1=Person("Rizwan",20)
p2=Person("Ranjith",22)

p1.greet()
p2.greet()