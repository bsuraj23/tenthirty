# Basic Exception Handling
try:
    num = int(input("Enter a number: "))
    print("Square is:", num ** 2)
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Handling Multiple Exceptions
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid integers only.")

# Using else and finally

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", x)
finally:
    print("This block always runs.")

# Custom Exception
class AgeTooSmallError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError("You must be 18 or older.")
    else:
        print("Age accepted.")
except AgeTooSmallError as e:
    print("Error:", e)
# Index Error Handling

try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range!")

# File Not Found Error
try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("The file does not exist.")
