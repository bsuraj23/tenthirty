from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Filter even numbers, square them, then sum
sum_of_squares = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
)

print("Sum of squares of even numbers:", sum_of_squares)
