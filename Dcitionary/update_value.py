#Update a key-value pair in a dictionary using a specific key
d={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
update_key = 'b'
if update_key in d:
    d[update_key] = 10
print("Updated dictionary key-value of b to 10:")
print(d)