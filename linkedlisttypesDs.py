# single linked list 
class node:
    def __init__(self,data):
       self.data=data
       self.next=None
head=node(10)
second=node(20)
third=node(30)
head.next=second
second.next=third
temp =head
while temp:
    print(temp.data) 
    temp=temp.next

# single linked list 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(10)
second = Node(20)
head.next = second

new_node = Node(30)
temp = head
while temp.next:
    temp = temp.next
temp.next = new_node

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

    #single linked list insert new node at first
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
head = node(40)
second = node(50)
third = node(60)
head.next = second
second.next = third
new_node = node(70)
new_node.next = head
head = new_node
temp = head
while temp:
    print(temp.data,end=" ->")
    temp = temp.next
    
# example 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create list: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# Delete first node
head = head.next

# Traverse
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next


# example 4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
prev = None
curr = head
while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
head = prev  # New head

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

# example 5
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = node(20)
head.next =node(30)
head.next.next = node(40)
count= 0
temp = head
while temp:
    count +=1
    temp = temp.next
    print("nodes:", count)

# search for value
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# List: 5 -> 15 -> 25
head = Node(5)
head.next = Node(15)
head.next.next = Node(25)

# Search for 15
temp = head
found = False
while temp:
    if temp.data == 15:
        found = True
        break
    temp = temp.next

print("Found!" if found else "Not found.")




# double linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
first = Node(10)
second = Node(20)
third = Node(30)

first.next = second
second.prev = first
second.next = third
third.prev = second

temp = third

while temp:
    print(temp.data)
    temp = temp.prev

 # inserting new node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 10 <-> 30
first = Node(10)
third = Node(30)

first.next = third
third.prev = first

# Insert 20 between 10 and 30
second = Node(20)
second.prev = first
second.next = third
first.next = second
third.prev = second
new_node =Node(25)
second.next = new_node
new_node.prev = second
new_node.next = third
third.prev = new_node

temp = first
while temp:
    print(temp.data, end=" , ")
    temp = temp.next
    # example 2
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
first=node(1)
second=node(2)
third=node(3)
first.next=second
second.prev=first
second.next=third
third.prev=second
temp=first
found = False
while temp:
    if temp.data == 2:
        found = True
        break
    temp = temp.next
print("node found:", found) 

# deleting the node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# 10 <-> 30
first = Node(10)
third = Node(30)

first.next = third
third.prev = first

# Insert 20 between 10 and 30
second = Node(20)
second.prev = first
second.next = third
first.next = second
third.prev = second
new_node =Node(25)
second.next = new_node
new_node.prev = second
new_node.next = third
third.prev = new_node

head = third
# deleting a node
node_to_delete = new_node
node_to_delete.prev.next = node_to_delete.next
node_to_delete.next.prev = node_to_delete.prev
temp = third
while temp:
    print(temp.data, end=" , ")
    temp = temp.next

  #  double
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Taking user input for 3 nodes (fixed for simplicity)
data1 = int(input("Enter first value: "))
data2 = int(input("Enter second value: "))
data3 = int(input("Enter third value: "))

first = Node(data1)
second = Node(data2)
third = Node(data3)

first.next = second
second.prev = first
second.next = third
third.prev = second

# Display list
temp = first
while temp:
    print(temp.data, end=" <-> ")
    temp = temp.next



# circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third
third.next = head

temp = head
while True:
    if temp.data == 20:
        break
    temp = temp.next
    if temp == head:
        break

new_node = Node(25)
new_node.next = temp.next
temp.next = new_node

temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == head:
        break

# example 2
class circular:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(100)
second = Node(200)
third = Node(300)

head.next = second
second.next = third
third.next = head
prev = None
curr = head
while True:
    if curr.data == 200:
        break
    prev = curr
    curr = curr.next
    if curr == head:
        break

if curr.data == 200:
    if curr == head: 
        last = head
        while last.next != head:
            last = last.next
        head = head.next
        last.next = head
    else:
        prev.next = curr.next
temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    temp == head

# insert at end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create circular list: 10 -> 20 -> 30 -> (back to 10)
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third
third.next = head  # Circular link

# Insert new node at end
new_node = Node(40)
temp = head
while temp.next != head:
    temp = temp.next
temp.next = new_node
new_node.next = head

# Traverse
temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == head:
        break
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create circular list: 10 -> 20 -> 30 -> (back to 10)
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third
third.next = head  # Circular link

# Insert new node at end
new_node = Node(40)
temp = head
while temp.next != head:
    temp = temp.next
temp.next = new_node
new_node.next = head

# Traverse
temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == head:
        break
# isert at beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create: 20 -> 30 -> (back to 20)
second = Node(20)
third = Node(30)
second.next = third
third.next = second  # Temporary head = second

# Insert 10 at beginning
new_node = Node(10)
new_node.next = second

# Find last node to update its next
temp = second
while temp.next != second:
    temp = temp.next
temp.next = new_node
head = new_node  # New head

# Traverse
temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == head:
        break

# delete a first node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third
third.next = head

# Delete first node (head)
temp = head
while temp.next != head:
    temp = temp.next

head = head.next
temp.next = head  
temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == head:
        break

# delete last node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# List: 1 -> 2 -> 3 -> (back to 1)
head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third
third.next = head

# Delete last node (3)
temp = head
while temp.next.next != head:
    temp = temp.next
temp.next = head  # Skip last node

# Traverse
temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == head:
        break
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# List: 1 -> 2 -> 3 -> (back to 1)
head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third
third.next = head

# Delete last node (3)
temp = head
while temp.next.next != head:
    temp = temp.next
temp.next = head  # Skip last node

# Traverse
temp = head
while True:
    print(temp.data, end=" -> ")
    temp = temp.next
    if temp == head:
        break


                      

   










    


