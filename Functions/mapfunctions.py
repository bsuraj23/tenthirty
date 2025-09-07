# Python program to demonstrate working of map.

def addition(n):
    return n + n

def subtraction(n):
    return n - n


numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


result = map(subtraction, numbers)
print(list(result))