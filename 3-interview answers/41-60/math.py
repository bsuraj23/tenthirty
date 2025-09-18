#Write a script with two modules, import one into the other, and call a function.
# main.py

# Import math_utils module
import math_utils

x = 5
y = 3

sum_result = math_utils.add(x, y)
mul_result = math_utils.multiply(x, y)

print(f"Sum of {x} and {y} is {sum_result}")
print(f"Product of {x} and {y} is {mul_result}")
