# even numbers using filter without lambda
def is_even(n):
    return n % 2 == 0
numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

#odd numbers using filter without lambda
def is_odd(n):
    return n % 2 != 0
numbers = [0,1,2,3,4,5,6,7,8,9]
odd_numbers = list(filter(is_odd, numbers))
print("Odd numbers:", odd_numbers)