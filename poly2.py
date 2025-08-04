class Parent:
  def test1(self):
    print("I am in Parent")
    
class Child(Parent):
  def test2(self):
    print("I am in Child") 

obj2 = Child()
obj2.test2()
# This raises attributeError!