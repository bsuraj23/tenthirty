# examples of stack
stack = []
stack.append(200)
stack.append(300)
stack.append(400)
print("stack:", stack)
print("poped:", stack.pop())
print("top element:", stack[-1])
print("Is stack empty:", len(stack)== 0)

# example 1
class Stack:
    def __init__(self):
        self.items = []
    def push(self, value):
        self.items.append(value)
    def pop(self):
        return self.items.pop() if not self.is_empty() else "Stack is empty"
    def peek(self):
        return self.items[-1] if not self.is_empty() else "Empty"
    def is_empty(self):
        return len(self.items) == 0
    def display(self):
        print("Stack:", self.items)
s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.display()
print("Popped:", s.pop())
s.display()

# example 2
def reverse_string(text):
    stack = []
    for ch in text:
        stack.append(ch)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str
print(reverse_string("python")) 

# example 3
stack =[]
stack.append("sumanth")
stack.append("saketh")
stack.append("prabhas")
while stack:
    print("popped:", stack.pop())


# example 4
class LimitedStack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, value):
        if len(self.stack) < self.size:
            self.stack.append(value)
        else:
            print("Stack Overflow!")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack Underflow!")

    def display(self):
        print("Stack:", self.stack)
s = LimitedStack(2)
s.push(10)
s.push(20)
s.push(30)  
s.display()
s.pop()
s.display()

# example 5
def decimal_to_binary(n):
    stack = []
    while n > 0:
        stack.append(str(n % 2))
        n //= 2
    binary = ""
    while stack:
        binary += stack.pop()
    return binary or "0"
print(decimal_to_binary(10))  
print(decimal_to_binary(0))   

# example 6
stack = []
numbers = [1, 2, 3, 4]
print("Original:", numbers)
for n in numbers:
    stack.append(n)
reversed_list = []
while stack:
    reversed_list.append(stack.pop())
print("Reversed:", reversed_list)

#example 7
from collections import deque
stack = deque()
stack.append("apple")
stack.append("banana")
stack.append("cherry")
print("stack:", stack)
print("popped:", stack.pop())
print("Top:", stack[-1])




