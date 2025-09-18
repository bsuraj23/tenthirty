#52.What are partial functions (`functools.partial`)?
numbers = [1, 2, 3, 4, 5]

# Multiply all numbers by 2 using partial
doubles = list(map(double, numbers))
print(doubles)  # [2, 4, 6, 8, 10]
