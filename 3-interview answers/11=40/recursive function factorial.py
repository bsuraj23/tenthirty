# Implement a recursive function to calculate factorial.
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive step
    return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
