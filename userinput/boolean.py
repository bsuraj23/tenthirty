a=input("Enter true or false: ")
b=input("Enter true or false: ")
if a == "true" and b == "true": 
    print("Both are true")
elif a == "true" and b == "false":
    print("First is true and second is false")
elif a == "false" and b == "true":
    print("First is false and second is true")
else:
    print("Both are false")
              