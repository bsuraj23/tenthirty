#Python code to open the file in Read, Write & append mode

#To read a file
file = open("C:\\A MET\\Git\\tenthirty\\Practice\\example.txt.txt", "r")  # Make sure the file exists
content = file.read()
print(content)
file.close()

#to open a file in write mode
file = open("C:\\A MET\\Git\\tenthirty\\Practice\\example.txt.txt", "w")  # Overwrites existing content or creates new file
file.write("This is written using write mode.")
file.close()

#to append
file = open("C:\\A MET\\Git\\tenthirty\\Practice\\example.txt.txt", "a")  # Adds content to the end without deleting existing content
file.write("\nThis is added using append mode.")
file.close()

#Creating a file (to open and delete )

#create a file
file = open("newfile.txt", "x")  # 'x' mode creates a new file; gives error if it exists
file.write("This is a new file.")
file.close()

#open a file 
file = open("newfile.txt", "r")
print(file.read())
file.close()

#delete a file
import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")