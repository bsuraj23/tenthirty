#Exception Handling

#Write code to handle division by zero with try-except
try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

#Create a custom exception NegativeNumberError and raise it when a negative number is passed
class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    else:
        print("Number is valid:", n)

check_number(5)
check_number(-3)  

#Implement a function that retries division 3 times if an error occurs
def safe_division(a, b):
    attempts = 3
    while attempts > 0:
        try:
            return a / b
        except ZeroDivisionError:
            print("Division by zero! Attempts left:", attempts - 1)
            attempts -= 1
            b = int(input("Enter a new divisor: "))
    print("All attempts failed!") 

#Write code that handles multiple exceptions (ZeroDivisionError, ValueError)
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input (not a number)")

#Implement a safe file reader that handles FileNotFoundError
def safe_file_reader(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("Error: File not found!")

print(safe_file_reader("data.txt"))