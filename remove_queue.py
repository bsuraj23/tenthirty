#Clear the queue using deque
from collections import deque

# Create a queue
queue = deque(["apple", "banana", "cherry"])
print("Original queue:", queue)

# Remove all elements (clear the queue)
queue.clear()

print("Queue after clearing:", queue)



#Delete queue variable completely using del
from collections import deque

queue = deque([1, 2, 3])
print("Queue before deletion:", queue)

# Delete the entire queue object
del queue
