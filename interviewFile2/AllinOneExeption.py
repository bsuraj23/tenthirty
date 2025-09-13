class NegativeNumberError(Exception):
    """Raised when a negative number is passed where not allowed"""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Negative numbers not allowed")
    return x ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Custom Exception Caught:", e)

#multiple exeption at once
try:
    x= int("abc")/2
except (ZeroDivisionError, ValueError) as e:
    print("error occured ",e)    