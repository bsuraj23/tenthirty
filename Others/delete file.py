import os
file_path =r"c:\open\MR.sunil.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("file deleted .")
else:
    print("file is not found ")