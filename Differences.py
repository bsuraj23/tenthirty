#Queue
from queue import Queue
q=Queue()
q.put(1)
q.put(2)
print(q.get())

#Dequeue

from collections import deque
d =deque()
d.append(1)
d.appendleft(2)
print(d.pop())
print(d.popleft())

#Lifo Queue

from queue import LifoQueue
lq=LifoQueue()
lq.put(1)
lq.put(2)
print(lq.get())

#priority queue

from queue import PriorityQueue
pq=PriorityQueue
pq.put(2, 'Sanjay')
pq.put(1, 'Rizwan')