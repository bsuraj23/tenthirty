#  Implement a function that retries division 3 times if an error occurs.
def safe_divide_with_retries(a, b, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print(f"Attempt {attempt + 1}: Division by zero error. Retrying...")
            b = int(input("Enter a new denominator: "))
        except Exception as e:
            print(f"Attempt {attempt + 1}: Error - {e}. Retrying...")
            a = int(input("Enter a new numerator: "))
            b = int(input("Enter a new denominator: "))
        attempt += 1
    
    print("All retries failed. Returning None.")
    return None


# Example usage
print(safe_divide_with_retries(10, 0))
