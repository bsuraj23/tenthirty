#   Write code to handle division by zero with try-except.
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result
    finally:
        print("Division attempt completed.")


# Example usage
print(safe_divide(10, 2))   # Works fine
print(safe_divide(5, 0))    # Handles error
