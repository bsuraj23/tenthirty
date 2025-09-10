#Simple Function (No arguments, No return)
# def greet():   #We use only greet() (without any arguments) because the function greet is defined without parameters.
#     print("hello world!")
# greet()
# #Function with Arguments
# def add_numbers(a, b):
#     print("sum:",a+b)
# add_numbers(3, 4)  
# #Function with Return Value
# def multiply(a, b):
#     return a * b
# result = multiply(4, 5)
# print("multiplication:", result)  
# #Function with Default Arguments
# def greet(name = "Game"):
#     print("Hello", name)
# greet()   #default arg
# greet("saad")    #overriding the arg
#Function with Keyword Arguments :You specify which value goes to which parameter by name
# def student_info(name, age):    
#     print(f"name:{name}, age:{age}")
# student_info(name="saadwitha", age =20)    
# Function with Variable Number of Arguments :The *numbers syntax means the function can accept any number of arguments.
# def total_sum(*numbers):
#     return sum(numbers)

# print("Total:", total_sum(5, 10, 15, 20))
#Recursive Function (Factorial Example)
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# print("factorial of 4:",factorial(4))
#Lambda Function (Anonymous Function)
square = lambda x: x * x
print("square of 7:", square(7))