from collections import deque

queue = deque(["alice","bob","charlie"])

print(queue)
first = queue.popleft()

print(queue)