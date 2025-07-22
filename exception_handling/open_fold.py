try:
    open("non_existent_file.txt")
    #open(r"C:\Users\chman\OneDrive\Desktop\Python\Function\fun1.py")
except FileNotFoundError:
    print("File not found")
