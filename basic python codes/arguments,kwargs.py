#Do not to give like this because the first argument or the first parameter should be non default argument means it has no value, only it has
#argument and it is first argument
# def example_function(a=5, b):
#     return a + b  # This will raise a SyntaxError
# example_function(4,5)

#in python we have two types of arguments
# 1. arguments
def student(firstname, middlename="Harish", lastname="reddy"):
    print(firstname,middlename,lastname)
student("Arutla")  # 1 positional argument
student('Arutla','Santosh','Reddy')  # 3 positional aruguments
student('arutla','reddy')  # 2 positional arguments
student('arutla', 'harish') # 2 positional arguments


# 2. keyword arguments
def student(firstname, lastname ='Mark', standard ='Fifth'):
    print(firstname, lastname, 'studies in', standard, 'Standard')
# 1 keyword argument
student(firstname ='John')     
# 2 keyword arguments                 
student(firstname ='John', standard ='Seventh') 
# 2 keyword arguments 
student(lastname ='Gates', firstname ='John')