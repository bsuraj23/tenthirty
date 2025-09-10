file_path = r"C:\Users\Srikanth_09\Documents\Write mode.txt"

with open(file_path, 'r') as file:
    content = file.read()
    print("📖 File Content:")
    print(content)
