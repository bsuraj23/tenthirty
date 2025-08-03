from collections import deque

q = deque([10, 20, 30, 40, 50])

# Remove from front (FIFO behavior)
print("popleft():", q.popleft())

# Remove from end (stack behavior)
print("pop():", q.pop())

print("Remaining:", q)


#output:
#popleft(): 10
#pop(): 50
#Remaining: deque([20, 30, 40])

from queue import Queue

q = Queue()
for item in [10, 20, 30]:
    q.put(item)

# Remove using get()
print("get():", q.get())
print("get():", q.get())
print("Remaining size:", q.qsize())


#output:
#get(): 10
#get(): 20
#Remaining size: 1


from queue import LifoQueue

q = LifoQueue()
for item in [10, 20, 30]:
    q.put(item)

# Remove using get() — behaves like stack
print("get():", q.get())
print("get():", q.get())
print("get():", q.get())
print("Remaining size:", q.qsize())

#output:
#get(): 30
#get(): 20
#get(): 10
#Remaining size: 0

q = [10, 20, 30, 40]

# Remove from front (slow for big lists)
print("pop(0):", q.pop(0))

# Remove from end (fast)
print("pop():", q.pop())

print("Remaining:", q)

#output:
#pop(0): 10
#pop(): 40
#Remaining: [20, 30]
