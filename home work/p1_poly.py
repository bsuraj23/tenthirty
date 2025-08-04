class parent:
 def greet(self):
    print("hello from parent")
class child(parent):
  def greet(self):
    print("hello from child") 
obj=child()
obj.greet()  
