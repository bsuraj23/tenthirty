from queue import PriorityQueue
pq=PriorityQueue()

pq.put((4,"ab"))
pq.put((2,"ac"))
pq.put((0,"bc"))
pq.put((10,"abc"))
pq.put((8,'abc'))
pq.put((2,"aa"))

while not pq.empty():
    print(pq.get())