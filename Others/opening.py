with open(r"C:\Users\sunil\OneDrive\Desktop\MR.SUNIL\Hello.txt","w") as f:
    f.write("welcom to the file and ready to access")
with open(r"C:\Users\sunil\OneDrive\Desktop\MR.SUNIL\Hello.txt","r") as f:
     content = f.read
     print(content())
with open(r"C:\Users\sunil\OneDrive\Desktop\MR.SUNIL\Hello.txt","+a") as f:
     f.write("and we- are updating the file")