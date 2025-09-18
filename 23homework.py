import os
# File name
filename = "example.txt"

# 1. Create and Write to a File
with open(filename, "w") as file:
    file.write("This is the first line.\n")
print("File created and written.")

# 2. Read the File
with open(filename, "r") as file:
    content = file.read()
    print("Reading File Content:")
    print(content)

# 3. Append to the File
with open(filename, "a") as file:
    file.write("This is the appended line.\n")
print("Data appended to the file.")

# 4. Read Again After Appending
with open(filename, "r") as file:
    content = file.read()
    print("Reading File After Appending:")
    print(content)

# 5. Delete the File
if os.path.exists(filename):
    os.remove(filename)
    print("File deleted successfully.")
else:
    print("File does not exist.")
