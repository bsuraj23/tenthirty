from queue import LifoQueue

stack = LifoQueue(maxsize=5)

# Add some items first
stack.put(1)#add item 1
stack.put(2)
stack.put(3)
stack.put(4)

print(stack.get())  #Remove and return an item from the stack  Output: 4 (last in, first out)
print(stack.get())  # 


#nowait is used to put items into the stack instantly without waiting
stack.put_nowait(40) 
stack.put_nowait(50)  

print("Stack Size:", stack.qsize())  # Output: 4 (items: 1, 2, 40, 50)
