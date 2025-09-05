import os

# 1️⃣ Create & Write to a file
filename = "example.txt"
with open(filename, "w") as file:
    file.write("Hello, this is the first line.\n")

# 2️⃣ Read the file
with open(filename, "r") as file:
    print("🔹 Initial Read:")
    print(file.read())

# 3️⃣ Append to the file
with open(filename, "a") as file:
    file.write("Now we've appended this new line.\n")

# 4️⃣ Reopen & Read after appending
with open(filename, "r") as file:
    print("\n🔹 After Appending:")
    print(file.read())

# 5️⃣ Delete the file
if os.path.exists(filename):
    os.remove(filename)
    print("\n✅ File deleted successfully.")
else:
    print("\n⚠️ File does not exist.")
