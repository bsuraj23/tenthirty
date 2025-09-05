#how to remove  queue directly
#collections.deque (has a direct clear)

from collections import deque

q = deque([10, 20, 30])
q.clear()              # directly empties the deque
print(q)         

#Example using collections.deque (easiest)

from collections import deque

# Create a queue
queue = deque(["A", "B", "C", "D"])
print("Original queue:", queue)

# Remove one element (front)
queue.popleft()
print("After one dequeue:", queue)

# Remove all elements directly
queue.clear()
print("After clear():", queue)