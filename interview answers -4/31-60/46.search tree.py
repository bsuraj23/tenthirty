#46.Implement a balanced binary search tree in Python.
avl = AVLTree()
root = None

# Insert nodes
for key in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, key)

# In-order traversal (should be sorted)
avl.in_order(root)
# Output: 10 20 25 30 40 50

# Search for keys
print("\nSearch 25:", avl.search(root, 25))  # True
print("Search 60:", avl.search(root, 60))    # False
