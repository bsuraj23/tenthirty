#60.What are monads in functional programming, and can they be represented in Python?
def list_bind(xs, func):
    return [y for x in xs for y in func(x)]

print(list_bind([1, 2, 3], lambda x: [x, -x]))
# [1, -1, 2, -2, 3, -3]
