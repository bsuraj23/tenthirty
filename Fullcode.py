#Write mode('w') - creates file it doesn't exist, and overwrites it
with open(file_name, 'w')  as file:
    file.write("This is written using write mode. \n")

#Append mode('a') - adds content to the end of the file
with open(file_name, 'a') as file:
    file.write("This is added using append mode. \n")

#Read mode('r') - reads the file content
with open(file_name, 'r') as file:
    content = file.read()
    print("File content:\n" + content)