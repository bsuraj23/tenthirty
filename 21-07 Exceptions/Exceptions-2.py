try:
    open("this file")
except FileNotFoundError:
    print("file not found")

try:
    result=5+5
except:
    print("error")
else:
    print("Result is:",result)   #if the try code runs properly then the else code also runs