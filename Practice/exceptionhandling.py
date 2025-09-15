#handling division by zero
try:
    a = int(input("Enter Numerator:"))
    b = int(input("Enter Denominator:"))
    result = a/b
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#Custom Exception - NegativeNumberError
class NegativeNumberError(Exception):
    """custom exception for negative numbers."""
    pass
def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative number is not allowed!")
    return num
try:
    x = int (input("Enter a positive number:"))
    check_positive(x)
    print("you entered:", x)
except NegativeNumberError as e:
    print("Error:", e)

#Handle multiple exceptions
