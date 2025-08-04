class Calc:
    def add(self, a, b=0,c=0):
        return a + b + c
    def multiply(self, a, b=1):
        return a * b
    def subtract(self, a, b=0):
        return a - b
 
add1= Calc()
print(add1.add(0,5))  # Output: 5
print(add1.add(5, 10))  # Output: 15
print(add1.add(5, 10, 15))

sub1= Calc()
print(sub1.subtract(10, 5))  # Output: 5
print(sub1.subtract(10))  # Output: 10

mul1= Calc()
print(mul1.multiply(5, 10))  # Output: 50
print(mul1.multiply(5))  # Output: 5
