from queue import PriorityQueue

pq = PriorityQueue()

pq.put((2, "low priority"))
pq.put((1, "high priority"))
pq.put((3, "lowest priority"))

while not pq.empty():
    print(pq.get()[1])  