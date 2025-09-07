#The super() function cannot be in line 2 or 3.
class Parent():
   def __init__(self):
      print("Parent constructor")
def show(self):  # <- This is OUTSIDE the class
      print("This is parent class")
#This show(self) method is outside the Parent class due to indentation error. So, when you later use super().show() 
#Python throws an error because Parent has no method show().