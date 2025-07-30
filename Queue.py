# Queue implemented using a list
queue = []

# Enqueue elements (add to the end)
queue.append('Rizwan')
queue.append('Sanjay')
queue.append('Nithish')
queue.append('Chandu')

print("Initial Queue:", queue)

# Remove a specific element (not based on FIFO)
element_to_remove = 'Chandu'

if element_to_remove in queue:
    queue.remove(element_to_remove)
    print(f"'{element_to_remove}' has been removed from the queue.")
else:
    print(f"'{element_to_remove}' not found in the queue.")

print("Updated Queue:", queue)