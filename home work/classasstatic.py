#How to Make a Class as "Static" ?
 #1. Use Only @staticmethods Inside the Class
#Define all methods as static so you don’t need self or an object.

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Call methods directly using class name
print(Calculator.add(10, 5))       
print(Calculator.subtract(10, 3))  
