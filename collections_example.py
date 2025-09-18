#collections
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# 1. Counter example
print("Counter Example:")
word = "banana"
counter = Counter(word)
print(counter)

# 2. namedtuple example
print("\nnamedtuple Example:")
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"x = {p.x}, y = {p.y}")

# 3. OrderedDict example
print("\nOrderedDict Example:")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

# 4. defaultdict example
print("\ndefaultdict Example:")
dd = defaultdict(int)  # default value = 0
dd['apple'] += 1
dd['banana'] += 2
print(dd)

# 5. deque example
print("\ndeque Example:")
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)
