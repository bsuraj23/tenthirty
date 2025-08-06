#Can parent object access the child method

In object-oriented programming, a parent object (or superclass) cannot directly access a child class's specific methods unless:

The method is overridden in the parent class and called polymorphically.

The parent is holding a reference to a child object (upcasting), and the method is declared in the child only — then, it can only be accessed by downcasting.

✅ Example in Python
python
Copy
Edit
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

# Create object of Parent
p = Parent()
# p.child_method()  # ❌ Error: Parent object can't access child method

# Create object of Child
c = Child()
c.show()         # ✅ Inherited from Parent
c.child_method() # ✅ Child method

# Upcasting: parent reference to child object
p2 = Child()
p2.show()         # ✅ Calls parent's method
# p2.child_method()  # ❌ Error: child_method not in Parent class