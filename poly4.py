class MyClass:
  def __init__(self):
    self.total = 0

  def  add(self, a=0, b=0):
    self.total += a + b
    return self.total
  
# Create object
obj = MyClass()

# Call add with no parameters
print(obj.add())

# Call add with one parameter
#print(obj.add(5))

# Call add with two parameters
print(obj.add(9,10))