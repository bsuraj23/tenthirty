from functools import reduce
# A function to add two numbers 
def add(x, y):
    return x + y
# A sample list
numbers = [1, 2, 3, 4, 5]
# Use reduce to apply add() cumulatively
total = reduce(add, numbers)

print("Sum of numbers:", total)