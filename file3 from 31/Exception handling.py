#Exception handling
#31.Division by zero
try:
    x = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
#32.Custom exception
class NegativeNumberError(Exception):
    pass

def check(n):
    if n < 0:
        raise NegativeNumberError("n must be non-negative")
try:
    check(-5)
except NegativeNumberError as e:
    print("Caught custom exception:", e)
#33.Retry division
def safe_div(a, b):
    for _ in range(3):
        try:
            return a / b
        except ZeroDivisionError:
            print('retry')
    return None
print(safe_div(10, 2))  
print(safe_div(10, 0))
#34.Multiple exceptions (with input)
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    print(x / y)
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)
#35.Safe file reader
def safe_read(file):
    try:
        with open(file) as f:
            return f.read()
    except FileNotFoundError:
        return None
print(safe_read("existing.txt"))  10
print(safe_read("no_such_file.txt")) 