#suare list numbers without using lambda 
#Example 1: Using a for loop

numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print("Squares:", squares)

# Example 2: Using a function + map

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squares = list(map(square, numbers))
print("Squares:", squares)

# Example 3: Using list comprehension

numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print("Squares:", squares)
