class Parent:
  def __init__(self , name):
    self.name = name


class Child(Parent):
  def __init__(self, name, age):
    super().__init__(name)
#Claasas the parent class constractor
    self.age = age
child_obj = Child("ParentName", 10)
print(child_obj.name)
#Accessing parent's 'name' attribute using child object