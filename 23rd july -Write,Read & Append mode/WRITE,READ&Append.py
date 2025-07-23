file_path = r"C:\Users\Srikanth_09\Documents\Write mode.txt"

# Write Mode - Overwrites existing content
text_to_write = "This file is created using write mode in Python.\n"
with open(file_path, 'w') as file:
    file.write(text_to_write)
print("Write completed.")

# Read Mode - Reads current content
with open(file_path, 'r') as file:
    content = file.read()
    print("\n Content after Write:")
    print(content)

# Append Mode - Adds new content at the end
text_to_append = "This line is added using append mode.\n"
with open(file_path, 'a') as file:
    file.write(text_to_append)
print("Append completed.")

# Read Mode Again - Reads final content
with open(file_path, 'r') as file:
    final_content = file.read()
    print("\n Final Content after Append:")
    print(final_content)
