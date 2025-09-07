class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    @staticmethod
    def multiply(x, y):
        return x * y
    
#calling without creating object
print(Calculator.add(5, 5))
print(Calculator.multiply(5, 5))

#calling using object
obj = Calculator()
print(obj.add(5, 5))
print(obj.multiply(5, 5))