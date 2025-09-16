#  Create a custom exception `NegativeNumberError` and raise it when a negative number is passed.# Define custom exception
class NegativeNumberError(Exception):
    def __init__(self, value):
        super().__init__(f"Negative number not allowed: {value}")


# Function that raises the custom exception
def process_number(n):
    if n < 0:
        raise NegativeNumberError(n)
    return f"Processing number: {n}"


# Example usage
try:
    print(process_number(10))   # Works fine
    print(process_number(-5))   # Will raise exception
except NegativeNumberError as e:
    print("Caught an exception:", e)
