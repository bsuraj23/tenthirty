def find_length(data):
    count = 0
    for _ in data:
        count += 1
    return count

print("Length of 'hello':", find_length("hello"))
print("Length of [1, 2, 3, 4]:", find_length([1, 2, 3, 4])) 
print("Length of (10, 20, 30):", find_length((10, 20, 30))) 
