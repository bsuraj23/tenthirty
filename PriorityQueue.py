from queue import PriorityQueue

# Create a PriorityQueue
pq = PriorityQueue()

# Add elements with priorities (priority, value)
pq.put((2, "task low"))
pq.put((1, "task medium"))
pq.put((0, "task high"))

print("Priority Queue Output:")
while not pq.empty():
    priority, task = pq.get()
    print(f"Priority {priority} -> {task}")
