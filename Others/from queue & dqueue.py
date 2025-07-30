from queue import Queue


q = Queue()
q.put(14)
q.put(5)
print(q.get())  
print(q.get())  


from collections import deque

dq = deque()
dq.append(14)
dq.appendleft(5)
print(dq.pop())       
print(dq.popleft())  