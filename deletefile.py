import os
file_path =r"E:\open\sai.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("file deleted .")
else:
    print("file is not found ")