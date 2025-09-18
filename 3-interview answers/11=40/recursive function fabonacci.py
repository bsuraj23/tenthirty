# Implement a recursive function to compute Fibonacci numbers.
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
num = int(input("Enter n: "))
print(f"Fibonacci({num}) = {fibonacci(num)}")
