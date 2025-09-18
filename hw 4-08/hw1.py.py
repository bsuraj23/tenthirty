#Using the child object how we call the parent object using the same name
class Parent:
    def show(self):
        print("This is the Parent class method")

class Child(Parent):
    def show(self):
        print("This is the Child class method")
        
        # Call Parent class method using super()
        super().show()

        # Another way: Call Parent class method using class name
        Parent.show(self)

# Create child object
child_obj = Child()

# Call the 'show' method
child_obj.show()