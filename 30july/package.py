import os
import math
import random
import sys

cwd = os.getcwd()
print("Current working directory (os):", cwd)

number = 25
sqrt_num = math.sqrt(number)
print("Square root of 25 (math):", sqrt_num)

rand_num = random.randint(1, 100)
print("Random number between 1 and 100 (random):", rand_num)

print("Script name and arguments (sys):", sys.argv)
