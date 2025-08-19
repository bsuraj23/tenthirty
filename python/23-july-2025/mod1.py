file = open("myfile.txt", "r")

content = file.read()
print(content)
file.close #important line

file = open("file.txt","a+")

file.write("hello this ia a line")

file.seek(0)
content = file.read()
print("file content:")
print(content)
file.close()