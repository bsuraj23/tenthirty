#local variable
print("Using local Variable")
def local():
    name="Harish"   #---->local variable
    print("welcome",name)
local()

#global variable
print("Using global variable")
name="Reddy"
def greet():
    print("Hello",name)
greet()
print("welcome",name)


#both
print("Printing both variables")
name="Harish Reddy"
def show():
    name="Hanuman"
    print("Inside function:",name)
show()
print("Outside function:",name)


#changing global variable inside function
print("changing variable variable inside function")
count=5
def update_count():
    global count
    count=count+1
    print("inside function count:",count)
update_count()
print("Outside function count:",count)