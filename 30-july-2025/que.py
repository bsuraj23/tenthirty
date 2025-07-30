from collections import deque

queue = deque()

queue.append("dog")
queue.append("cat")
queue.append("penguin")

print(queue[0])
print(queue)
print(len(queue))
animal = queue.pop()

print(queue)