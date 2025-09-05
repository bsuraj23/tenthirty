 # Basic Try-Except

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")

# Handling Multiple Exceptions

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Try-Except-Else Block

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number.")
else:
    print("You entered:", num)

# Try-Except-Finally

try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("This will run no matter what.")

# Custom Exception Example

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative number entered!")
    print("You entered:", num)
except NegativeNumberError as e:
    print(e)

