class Parent:
  def test1(self):
    print("I am in Parent")
    
class Child(Parent):
  def test2(self):
    print("I am in Child") 

obj1 = Parent()
obj1.test1()
# This raises attributeError!