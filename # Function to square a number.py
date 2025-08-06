# Function to square a number
def square(x):
    return x * x

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Apply the function using map
squared_numbers = list(map(square, numbers))

# Print result
print("Squared numbers:", squared_numbers)