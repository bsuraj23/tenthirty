#Functions

#function that takes *args and **kwargs and prints them separately
def print_args_kwargs(*args, **kwargs):
    print("Arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)
print_args_kwargs(1, 2, 3, name="Alice", age=25)

#Implement a recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  

print("Factorial of 5:", factorial(5))  

#Implement a recursive function to compute Fibonacci numbers
def fibonacci(n):
    if n <= 1:  
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(10):
    print(fibonacci(i), end=" ")

#a function that accepts a list and returns a new list with only unique elements
def unique_elements(lst):
    return list(set(lst))  
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", unique_elements(numbers))

#function that returns the sum of digits of a number
def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total
print("Sum of digits of 12345:", sum_of_digits(12345)) 