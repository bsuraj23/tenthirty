 #Print even numbers using filter() (no lambda)
def is_even(n):
    return n % 2 == 0

numbers = [11, 22, 33, 44, 55, 66]
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

# 2. Print odd numbers using filter() (no lambda)
def is_odd(n):
    return n % 2 != 0

numbers = [11, 22, 33, 44, 55, 66]
odd_numbers = list(filter(is_odd, numbers))
print("Odd numbers:", odd_numbers)