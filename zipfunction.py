# Define two lists
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

# Use zip to pair each name with a score
combined = zip(names, scores)

# Convert the zip object to a list and print it
combined_list = list(combined)
print(combined_list)


for name, score in zip(names, scores):
    print(f"{name} scored {score}")
