from queue import Queue


q = Queue()
q.put(69)
q.put(96)
print(q.get())  # 10
print(q.get())  # 20


from collections import deque

dq = deque()
dq.append(69)
dq.appendleft(96)
print(dq.pop())       # 10
print(dq.popleft())   # 5