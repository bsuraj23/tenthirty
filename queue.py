from Queue import Queue

q = Queue()
q.put(1)             # Enqueue
q.put(2)
print(q.get())       # Dequeue → 1
print(q.get())       # Dequeue → 2
