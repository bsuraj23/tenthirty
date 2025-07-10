list=["1","2",23,45.321]
print(list)
print(type(list))
print(list[0])
list.append("new toy")
print(list)
print(list[0:3])
#inserting an item at index 3
# This will shift the existing items at index 3 and beyond to the right
list.insert(3,"5000")
print(list)
#appending an item at the end of the list
list.append("Manish")
print(list)