class AgeTooSmallError(Exception):
    """Raised when the entered age is less than 18"""
    pass

try:
    age=int(input("Enter the age:"))
    if age<18:
        raise AgeTooSmallError("Age must be atleast 18 to register")
    print( "Successtion Registration")
except AgeTooSmallError as a:
    print("Error:", a)
    
#custom exception is not the default provided exception by python, we create it own exception that is called custom exception
#we inherits from built-in modules with a child class, the Exception class is the parant class in built-in module from 
#here we inherits with the child class.

