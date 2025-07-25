file=open("creating file.txt",'w')  #creating and writing
file.write("Hello, this is Harish, Iam creating file here\nWelcome to my file.")
file.close()

file=open("creating file.txt",'r')   #reading
read=file.read()
print("File content:")
file.close()

file=open("creating file.txt",'a')         #append
file.write("\nThis line is added later.")
file.close()



file=open("creating file.txt",'r')   #reading line by line
print("\nRead line by line:")
for line in file:
    print(line.strip())
file.close()


import os
if os.path.exists("creating file.txt"):    #checking if the file is existing or not
    print("\n File is found")
else:
    print("File Not found!")

os.rename("creating file.txt","file2.py")   #it only runs one time when the file name is renamed,
print("File renamed to 'file2.py'")         #if you run more than one time it will get error the file is already exist!


os.remove("file2.py")                     #removing
print("file deleted successfully")





