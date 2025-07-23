with open(r"C:\udayyy\uday goud.txt","w") as f:
    f.write("welcom to the file and ready to access")
with open(r"C:\udayyy\uday goud.txt","r") as f:
     content = f.read
     print(content())
with open(r"C:\udayyy\uday goud.txt","+a") as f:
     f.write("and we- are updating the file")