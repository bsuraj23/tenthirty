#Simple Input Error Handling

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("Something went wrong! Please enter a valid number.")
    
# Divide by Zero Handling

try:
    a = 10
    b = 0
    print(a / b)
except:
    print("Cannot divide by zero!")
# Multiple Exceptions

try:
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))
    print("Result:", x / y)
except ValueError:
    print("Enter only numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
# File Not Found

try:
    f = open("file.txt", "r")
    print(f.read())
except:
    print("File not found.")
 # Using finally

try:
    print("Try block running.")
except:
    print("Something went wrong.")
finally:
    print("This will always run.")
