from queue import LifoQueue
stack = LifoQueue(maxsize=5)
stack.put(1)
stack.put(2)    
stack.put(3)
stack.put(4)
print("Stack Size:",stack.qsize())