with open(r"C:\dheeraj\demo.txt","w") as f:
    f.write("welcom to the file and ready to access")
with open(r"C:\dheeraj\demo.txt","r") as f:
     content = f.read
     print(content())
with open(r"C:\dheeraj\demo.txt","+a") as f:
     f.write("and we- are updating the file")