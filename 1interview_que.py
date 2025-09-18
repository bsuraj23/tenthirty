##Reverse a string with using slicing
# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("python"))  # Output: nohtyp


#difference between set and tuple
#set have {} curly brackets,it doesnot allow duplicate value,add or remove the values
#tuple have() brackets,it allow the duplicate values, once created we cannot add or remove the values
# set = {1,2,3}
# print(set)
# tuple = (4,6,8)
# print(tuple)

#Features of Python and its portability
# Simple & Easy to Learn ,High-Level Language
# Interpreted Language ,Platform Independent (Portability)
# Dynamically Typed
#Portability means the ability to run the same code on different platforms (Windows, Linux, Mac, etc.) without modification.
# hello.py
# print("Hello, World!")
# You can run hello.py on Windows, Linux, or macOS without changing the code.
# Why is Python portable?
# It is interpreted, not compiled.
# The Python interpreter is available for almost all operating systems.
# Follows “Write Once, Run Anywhere” principle (as long as the required libraries are available).

#is python compiler or interpreter why
# Python is an interpreted language
# When you run a Python program, it does not convert the whole code into machine code at once (like a compiler).
# Instead, Python executes the code line by line using the Python interpreter.
# Process of Execution in Python
# You write a program → program.py
# Python internally uses a compiler + interpreter combination:
# First, Python compiles the source code into bytecode (.pyc files).
# Then, the Python Virtual Machine (PVM) (interpreter) executes this bytecode line by line

#difference between fastapi, django and flask
# Django is a high-level, full-stack Python web framework that comes with many built-in features like ORM, admin panel, authentication, and templating, making it ideal for building large and complex web applications.
# Flask is a lightweight and minimal Python web framework (microframework) that provides only the essential tools for web development, leaving developers free to add extensions as needed, making it flexible and easy to learn.
# FastAPI is a modern, high-performance Python web framework designed for building APIs quickly, with automatic documentation (Swagger, ReDoc), async support, and fast execution speed, making it suitable for microservices and data-driven applications.
# 👉 In short:
# Django → Full-featured, best for big apps.
# Flask → Minimal, best for small apps.
# FastAPI → Fast, modern, best for APIs.


#beginner coding questions
#Reverse a string without using slicing
# def reverse_string(s):
#     rev = ""
#     for char in s:
#         rev = char + rev
#     return rev
# print(reverse_string("python")) 


#Find the largest number in a list
# def largest_number(lst):
#     max_num = lst[0]      #out of range
#     for num in lst:
#      if num > max_num:
#         max_num = num
#     return max_num
# print(largest_number([0,22,44,6,1,100,99]))


##Find the smallest number in a list
# def smallest_number(lst):
#     min_num = lst[0]      #out of range
#     for num in lst:
#       if num < min_num:
#         min_num = num
#     return min_num
# print(smallest_number([10,22,44,6,1,100,99]))


#Count vowels in a string
# def count_vowels(s):
#    vowels = "aeiouAEIOU"
#    count = 0
#    for char in s:
#       if char in vowels:
#          count += 1
#    return count
# print(count_vowels("Hello! Wellcome to python"))    


#Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # check till sqrt(n)
        if n % i == 0:
            return False
    return True

print(is_prime(22))   
print(is_prime(11))  
