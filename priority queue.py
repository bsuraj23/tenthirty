import queue
pq = queue.PriorityQueue()
pq.put((3, 'Sanjay'))
pq.put((1, 'Rizwan'))
pq.put((2, 'Nithish'))

print("Process tasks in order:")
while not pq.empty():
    priority, task=pq.get()
    print(f"priority{priority}:{task}")