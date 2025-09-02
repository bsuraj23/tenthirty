file=open("creating file.txt",'w')    # creating and wrinting
file.write("Iam sumanth")
file.close()

file=open("creating file.txt",'r')     # r means reading
read=file.read()
print("file content")
file.close()

file=open("creating file.txt",'a')     # a means append
file.write("\nThis line is added later.")
file.close()

file=open("creating file.txt",'r')     # reading line by line
print("Read line by line:")
for line in file:
    print(line.strip())
file.close()

import os                                  #checking file existing or not
if os.path.exists("creating file.txt"):
    print("\n file is found")
else:
    print("\n file not found!")

os.rename("creating file.txt","file3.py")   # it will run only one time next we have to change file name  
print("file renamed to 'file3.py'")   #if we run more than one time it will show already exist


os.remove("file3.py")              # remove
print("file deleted sucessfully")