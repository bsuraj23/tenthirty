#If you want to use a stack in Python, you can use a list.
stack = []

# Add some items first
#to add element in the stack, use append() method and in queue use put() method
stack.append(1)  # add item 1
stack.append(2)
stack.append(3)
stack.append(4)

print(stack.pop())  # Remove and return an item from the stack  Output: 4 (last in, first out)
print("After pop/removing element :",stack)