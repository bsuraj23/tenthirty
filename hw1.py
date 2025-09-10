In object-oriented programming (OOP), a parent object (or class) cannot directly access the methods of a child class, unless 
those methods are:
Overridden in the child class, and Called through a child class reference.

Why?
The parent class doesn't "know" what specific methods its child classes have — it only knows about itself and its own methods.

❌ Parent object cannot access child-specific methods.
✅ Child object can access both parent and its own methods.
✅ Polymorphism allows child overrides to be used when using parent references.

 A Parent class object cannot directly access child class method that are not declared in the parent class. If a variables is of the parenttype, you can only callmethods defind in the parent class interface.Child only methods are not accessible unless you cast the object to the child type.



class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

# Parent object
p = Parent()
p.show()          # ✅ Works (Parent method)
# p.child_method()  # ❌ Error: 'Parent' object has no attribute 'child_method'






