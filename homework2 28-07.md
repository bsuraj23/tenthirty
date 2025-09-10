#Can super() function be in second or third line

Yes, the super() function can be on the second or third line in a method — there is no restriction that it must be the first line.

However, it is usually called at the beginning of the method to ensure that the parent class initialization or behavior is executed before the child adds or modifies anything.

✅ Example – super() in the second line
python
Copy
Edit
class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        print("Child constructor - line 1")
        super().__init__()  # ✅ called in second line
        print("Child constructor - line 3")

c = Child()