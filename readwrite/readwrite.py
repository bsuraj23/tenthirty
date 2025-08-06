# File name
filename = "example_file.txt"

# Step 1: Write to the file (this creates or overwrites the file)
with open(filename, 'w') as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
print("Data written to file.")

# Step 2: Append more content to the same file
with open(filename, 'a') as file:
    file.write("This line is appended.\n")
    file.write("Another appended line.\n")
print("Data appended to file.")

# Step 3: Read and print the content of the file
with open(filename, 'r') as file:
    content = file.read()
print("File content:\n")
print(content)
