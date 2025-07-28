class Parent:
    def show(self):
        print("This is the method shown in parent class")
class Child(Parent):
    def Child_method(self):
        print("This is the method shown in child class")

p = Parent()
p.show()

c = Child()
c.show()
c.Child_method()
        