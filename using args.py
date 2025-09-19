def add_numbers(*args):
    """Add any number of numbers"""
    total = 0
    for num in args:
        total += num
    return total

# Using the function
print(add_numbers(2, 3))           
print(add_numbers(1, 2, 3, 4, 5))  
print(add_numbers())