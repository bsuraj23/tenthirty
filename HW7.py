can super function in 2nd or 3rd line?
Yes, the super() function can be used anywhere inside a method — not just in the first line. It is commonly used at the beginning of a method (especially in constructors) to ensure proper initialization of the parent class, but it’s not restricted to the first line.

program:

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method starts")
        super().show()  # Using super in 2nd line
        print("Child method ends")

c = Child()
c.show()

So yes — super() can be used in any line within a method where accessing the parent class is needed.









