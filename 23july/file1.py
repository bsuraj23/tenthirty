import os

with open ("file1.txt","w") as file1 : 
    file1.write("my name is soham")   # here file is created and wrote a line
    print("file is created")
    
with open ("file1.txt","r") as file1:
    content=file1.read()               # here we read the file
    print(content)
    
if os.path.exists("file1.txt") :
    os.remove("file1.txt")
    print("file is deleted ")    # here delete file if it exists
    
else :
    print("file not exists ")
    
    
        