#58.What is the difference between map/filter/reduce and comprehensions?
# map equivalent
squared = [x**2 for x in nums]

# filter equivalent
evens = [x for x in nums if x % 2 == 0]

# reduce has no direct comprehension form → usually use `sum()`, `math.prod()`
total = sum(nums)
