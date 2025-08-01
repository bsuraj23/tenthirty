from queue import PriorityQueue

a=PriorityQueue()
a.put(("Apple"))
a.put(("Lemon"))
a.put(("Banana"))

while not a.empty():
    print(a.get())