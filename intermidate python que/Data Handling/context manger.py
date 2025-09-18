# Writing to a file using context manager
with open("example.txt", "w") as file:
    file.write("Hello, this is written using context manager swathi!")

# Reading from the file using context manager
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
