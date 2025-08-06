#for Compile
# Python source code as a string
source_code = """
for i in range(3):
    print("Hello from compiled code:", i)
"""

# Compile the source code string into a code object
compiled_code = compile(source_code, filename="<string>", mode="exec")

# Execute the compiled code
exec(compiled_code)

#for queue
from queue import Queue

q = Queue()
q.put(1)
q.put(2)
print(q.get()) 

#for Deque
from collections import deque

d = deque()
d.append(1)
d.append(2)
print(d.popleft())

#for math
import math

# Basic constants
print("Pi:", math.pi)
print("Euler's number (e):", math.e)

# Square root
print("Square root of 16:", math.sqrt(16))

# Power
print("2 raised to the power 5:", math.pow(2, 5))  # Same as 2**5

# Trigonometry
angle = math.radians(90)  # Convert degrees to radians
print("Sin(90 degrees):", math.sin(angle))

# Logarithms
print("Log base e of 10:", math.log(10))
print("Log base 10 of 1000:", math.log10(1000))

# Factorial
print("Factorial of 5:", math.factorial(5))

# Ceiling and floor
print("Ceiling of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))

#for random
import random

# Generate a random number between 1 and 10
num = random.randint(1, 10)

print("Random number is:", num)

# importing calendar module
import calendar

yy = 2003  # year
mm = 8    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

#for priorityqueue
import queue

# Create a priority queue
pq = queue.PriorityQueue()

# Add items with priorities (lower number = higher priority)
pq.put((1, "Task with Priority 1"))
pq.put((3, "Task with Priority 3"))
pq.put((2, "Task with Priority 2"))

# Get items in order of priority
while not pq.empty():
    priority, task = pq.get()
    print(f"{task} (Priority: {priority})")

#collections (Counter)
from collections import Counter
print(Counter("banana").most_common(1))

#LIFO queue
import queue

# Create a LIFO queue (stack)
stack = queue.LifoQueue()

# Push items (add to top)
stack.put("Item 1")
stack.put("Item 2")
stack.put("Item 3")

# Pop items (remove from top)
while not stack.empty():
    item = stack.get()
    print("Popped:", item)
