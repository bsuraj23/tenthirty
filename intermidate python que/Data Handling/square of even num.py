numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: filter even numbers
evens = filter(lambda x: x % 2 == 0, numbers)

# Step 2: square the even numbers
squares = map(lambda x: x ** 2, evens)

# Convert to list for display
result = list(squares)
print("Squares of even numbers:", result)
