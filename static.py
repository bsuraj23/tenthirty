class MathUtils:
  @staticmethod
  def add(a, b):
    return a + b
  
  @staticmethod
  def sub(a, b):
    return a - b
  
  @staticmethod
  def multiply(a, b):
    return a * b
  
  @staticmethod
  def divide(a, b):
    if  b == 0:
      raise
ValueError("Cannot divide by zero.")

# Usage (no object instantiation needed):
print(MathUtils.add(10, 5))
print(MathUtils.sub(10, 5))
print(MathUtils.multiply(10, 5))
print(MathUtils.divide(10, 5))
  
  

  
  
  