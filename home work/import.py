import math

# Square root
print("Square root of 16:", math.sqrt(16))

# Power
print("2 raised to 3:", math.pow(2, 3))

# Absolute value
print("Absolute value of -5:", math.fabs(-5))

# Factorial
print("Factorial of 5:", math.factorial(5))
#math
import math

print("Pi value:", math.pi)
print("Euler's number (e):", math.e)

#calendar

import calendar
print(calendar.month(2025, 12))  # Show december 2025 as a text calendar

# random
import random
colors = ["red", "green", "blue"]
print(random.choice(colors))  # Randomly picks one item

#collections (Counter)
from collections import Counter
print(Counter("banana").most_common(1))  # [('a', 3)]

# deque
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)       # add to right
print(dq.popleft())  # remove from left -> 1
print(dq)            # deque([2, 3, 4]

# queue.Queue (FIFO)
import queue
q = queue.Queue()
q.put("task1")
q.put("task2")
print(q.get())  # 'task1'

# queue.LifoQueue (stack)
import queue
stk = queue.LifoQueue()
stk.put("first")
stk.put("second")
print(stk.get())  # 'second'

# compile (built-in)
code = compile("2 + 3 * 4", "<expr>", "eval")
print(eval(code))  # 14

# queue.PriorityQueue
import queue
pq = queue.PriorityQueue()
pq.put((2, "medium"))
pq.put((1, "high"))
pq.put((3, "low"))
print(pq.get())  # (1, 'high')  -> lowest number = highest priority