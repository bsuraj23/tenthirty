with open("file2.txt","w") as file2:
    file2.write("file 2 is created")

with open("file2.txt","r") as file2:
    content = file2.read()
    print(content)
    
with open("file2.txt","+a") as file2:
    file2.write("\n this is new content that we appended")
    print("we appended the text")
   
    
with open("file2.txt") as file2:
    newcontent= file2.read()
    print(newcontent)         