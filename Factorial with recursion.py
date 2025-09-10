#Factorial with recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)
num = int(input("Enter the value:"))
print(f"Factorial of {num} is {factorial (num)}")
