class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Build simple list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Traverse
curr = head
while curr:
    print(curr.data)
    curr = curr.next
