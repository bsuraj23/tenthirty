from collections import deque

d=deque()
d.appendleft(1)
d.append(4)

print(d)



#poping single element
d.popleft()
print(d)


#clearing total deque
# d.clear()
# print(d)