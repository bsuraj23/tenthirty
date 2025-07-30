from queue import Queue
q = Queue()
q.put(789)
q._put(2012)
q.put(45)
print(q.get())
print(q.get())
print(q.get())

from collections import deque

dq = deque()
dq.appendleft(12)
dq.append(56)
dq.appendleft(58)
print(dq.popleft())
print(dq.pop())

