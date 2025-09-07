class Parent():
   def __init__(self):
      print("Parent constructor")
def show(self):
      print("This is parent class")

class Child(Parent):
   def __init__(self):
      super().__init__()
      print("Child consturctor")
def show(self):
         super().show()
         print("This is child class") 

c = Child()
c.__init__()           