#43.Implement a custom linked list class with `insert`, `delete`, and `search`.
ll = LinkedList()

# Insert elements
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.print_list()
# Output: 10 -> 20 -> 30 -> None

# Search elements
print(ll.search(20))  # True
print(ll.search(40))  # False

# Delete elements
ll.delete(20)
ll.print_list()
# Output: 10 -> 30 -> None

ll.delete(10)
ll.print_list()
# Output: 30 -> None
