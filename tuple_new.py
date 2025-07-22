my_tuple = (1,2,3,4,5)
print("original tuple:", my_tuple)
print("Element at index 2:", my_tuple[2])
print("sliced tuple (index 1 to 3):", my_tuple[1:4])
another_tuple = (6,7,8)
concatenated_tuple = my_tuple + another_tuple
print("concatenated tuple:", concatenated_tuple)
repeated_tuple = my_tuple*2
print("repeated tuple:", repeated_tuple)
print("count of element 2:", my_tuple.count(2))