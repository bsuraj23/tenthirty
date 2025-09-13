#LEGB rule in python
x= "global valiable"

def outer():
    y= "enclosing variable"
    
    def inner():
        z= "local variable"
        print(z)
    
    inner()

outer() # local variable

#difference between local and global
a=5
def abc():
    b=6
    print(b)
    
abc()  #6
print("global variable :",a)    # you cannot print b here

#how to use global variable in function
count=0
def xcv():
    global count  # compalsary to use global keyword
    count+=1

xcv()
print(count)    #1

#how to use nonlocal variable in function
def asd():
    x= 4
    def ghj():
        nonlocal x
        x+=1
        print("inner:",x)
    ghj()
    print("outer x:",x)

asd()

# what if all variable have same name -> python will follow LEGB rule

x="global"
def outer():
    x="enclosing"
    def inner():
        x= "local"
        print(x)
    inner()    
    print(x) 
    
outer()
print(x)       
          