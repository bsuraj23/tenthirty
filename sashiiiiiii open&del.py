import os
file_path =r"D:\sashiiiiii\sashi kiran.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("bahubali .")
else:
    print("bahubali")