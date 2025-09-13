
#ZeroDivideError
a= 0
try:
    10/a
except ZeroDivisionError:
    print("you cannot divide by zero IDIOT")
    
finally:
    print("last line")  
    
              
#Value error

try:
    st= int(input("enter a number"))

except ValueError:
    print("you are asked to type number ")    
    
finally:
    ("last line")                  
    
#TypeError
try:
    result= 55+"soham"
except TypeError as e :
    print(" error occured",e)
finally:
    print("last line")            