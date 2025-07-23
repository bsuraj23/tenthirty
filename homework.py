import os
# File name
file_name = "sample.txt"

# Step 1: Create and Write to the File
with open(file_name, "w") as file:
    file.write("Hello, this is the first line.\n")
print("Step 1: File created and data written.")

# Step 2: Append Data to the File
with open(file_name, "a") as file:
    file.write("This is an appended line.\n")
print("Step 2: Data appended to the file.")

# Step 3: Read the File
with open(file_name, "r") as file:
    content = file.read()
print("Step 3: File content after write and append:")
print(content)

# Step 4: Delete the File
if os.path.exists(file_name):
    os.remove(file_name)
    print("Step 4: File deleted.")
else:
    print("The file does not exist.")