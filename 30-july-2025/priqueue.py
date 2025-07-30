from queue import PriorityQueue

# print(dir(PriorityQueue))

pq = PriorityQueue()

pq.put(1,"Emergency Heart attack")

pq.put(3,"flu")
pq.put(2, "broken arm")

while not pq.empty():
    print(pq.get()[1])