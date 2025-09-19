#Functional Programming
#56.map square
result = list(map(lambda x: x * x, [1, 2, 3]))
print(result)
#57.filter even
result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(result)
#58.reduce product
from functools import reduce

result = reduce(lambda a, b: a * b, [1, 2, 3])
print(result)
#59.Lambda sort by second element
lst = [(1, 3), (2, 2)]
sorted_lst = sorted(lst, key=lambda x: x[1])
print(sorted_lst)
#60.map + filter + reduce (sum of squares of even numbers)
from functools import reduce

lst = [1, 2, 3, 4]

# 1. Filter evens
even = filter(lambda x: x % 2 == 0, lst)    # yields 2,4

# 2. Square them
squares = map(lambda x: x * x, even)        # yields 4,16

# 3. Sum them
total = reduce(lambda a, b: a + b, squares) # 4+16

print(total)