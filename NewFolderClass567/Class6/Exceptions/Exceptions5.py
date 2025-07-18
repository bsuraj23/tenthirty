try:
    open("nonexistent.txt")
except FileNotFoundError:
    print("File does not exist")
