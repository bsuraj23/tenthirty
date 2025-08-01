from queue import LifoQueue

stack=LifoQueue()
stack.put('a')
stack.put('A')

print(stack.get())
print(stack.get())