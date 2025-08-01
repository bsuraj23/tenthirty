from queue import Queue
q=Queue()
q.put(10)
q.put(20)
print(q.get())
print(q.get())
queue=[]
q1=queue
q1.append(30)
q1.append(40)
print(q1)
q1.pop()
print(q1)