#  Write code that handles multiple exceptions (e.g., `ZeroDivisionError`, `ValueError`).
def safe_divide():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid integers only.")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation completed.")


# Example usage
safe_divide()
