#Functions

#function with *args and **kwargs
def print_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
print_args_kwargs(1, 2, 3)

#Recursive Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print (factorial(120))


#unique elements from a list
def unique_elements(lst):
    return list(set(lst))
print (unique_elements([1,2,2,3,4,4,5,6,7,7,8]))

#to print sum of digits
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
print(sum_of_digits(12345))

