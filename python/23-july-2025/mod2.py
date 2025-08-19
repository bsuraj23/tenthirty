import os 

file = "mod13.txt"

if os.path.exists("mod3.txt"):
    os.remove("mod3.txt")
    print("deleted")
