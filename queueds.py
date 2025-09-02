# programs on queue
queue = []
queue.append(12)
queue.append(13)
queue.append(14)
print("Queue:", queue)
print("Dequeued:", queue.pop(0))
print("After dequeue:", queue)

# example 2
from  collections import deque
queue = deque()
queue.append(33)
queue.append(34)
queue.append(35)
print("Queue:", queue)
print("Dequed:", queue.popleft())
print("Dequed:", queue.popleft())
print("after dequeue:", queue)

# example 3
class queue:
    def __init__(self):
        self.items = []
    def enqueue(self, items):
        self.items.append(items)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[0] if not self.is_empty() else "Empty"
    def display(self):
        print("Queue:", self.items)
q = queue()
q.enqueue(23)
q.enqueue(24)
q.enqueue(25)
q.display()
print("Front:", q.peek())
print("Dequed:", q.dequeue())
q.display()

#example 4
class BoundedQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, data):
        if len(self.queue) < self.size:
            self.queue.append(data)
        else:
            print("Queue is full")

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def display(self):
        print("Queue:", self.queue)
bq = BoundedQueue(3)
bq.enqueue(10)
bq.enqueue(20)
bq.enqueue(30)
bq.enqueue(40)  
bq.display()
bq.dequeue()
bq.display()

# example 5
from collections import deque
queue = deque()
queue.append(90)
queue.append(91)
queue.appendleft(60)
print("Queue:", queue)
print("rear removed:", queue.pop())
print("front removed:", queue.popleft())
print("remaining queue:", queue)

# example 6
from collections import deque
q = deque()
word = "python"
for ch in word:
    q.append(ch)
while q:
    print(q.popleft(), end=" ")

# example 7
queue = []
queue.append(("Alice", 22))
queue.append(("Bob", 25))
queue.append(("Carol", 27))
while queue:
    person = queue.pop(0)
    print("Name:", person[0], "| Age:", person[1])

# example 8
from collections import deque
def is_palindrome(string):
    q = deque(string)
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True
print(is_palindrome("madam")) 
print(is_palindrome("hello"))  

    

    















