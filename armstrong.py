def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d)**power for d in digits)

print(is_armstrong(153)) 

from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)