from collections import deque

dq = deque()
dq.append('a')       # Add to right
dq.appendleft('b')   # Add to left
print(dq.pop())      # Remove from right → 'a'
print(dq.popleft())  # Remove from left → 'b'
