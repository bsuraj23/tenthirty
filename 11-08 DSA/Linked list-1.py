class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)

#inserting in the middle
current=head
while current:
    if current.data==2:
        new_node=Node(10)
        new_node.next=current.next
        current.next=new_node
        break
    current=current.next

#deleting
current=head
while current and current.next:
    if current.next.data==3:
        current.next=current.next.next
        break
    current=current.next

#printing
current=head
while current:
    print(current.data, end="->")
    current=current.next
print(None)