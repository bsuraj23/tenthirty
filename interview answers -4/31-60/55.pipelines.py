#55.How do you implement functional pipelines in Python?
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = pipe(
    numbers,
    lambda xs: map(lambda x: x * 2, xs),       # double
    lambda xs: filter(lambda x: x % 2 == 0, xs), # keep evens
    lambda xs: reduce(lambda a, b: a + b, xs)  # sum
)

print(result)  # 20
