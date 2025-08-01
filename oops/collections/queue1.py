from queue import Queue

q2 = Queue()  # This queue is created but not used
q1 = Queue()  # Active queue

# Add elements to q1
q1.put(10)
q1.put(20)


# Remove and print elements from q1
print(q1.get())  # First 10
front=q1.queue[0]
print(front)
print(q1.empty())
