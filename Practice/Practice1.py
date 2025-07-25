# Exceptions

#1 ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero error")

#2 ValueError
try: 
    int('Deepthi')
except ValueError:
    print("Invalid")

#3 IndexError
try:
    list=[1,2,3]
    print(list[5])
except IndexError:
    print("IndexOut of Range")

#4 KeyError
try:
    a = {"b":2}
    print (a["z"])
except KeyError:
    print("Key not found")

#5 FileNotFoundError
try:
    open("abc.txt")
except FileNotFoundError:
    print("File Not Found")

#6 ModuleNotFoundError
try:
    import non_existing_module
except ModuleNotFoundError:
    print("Module Not Found")

#7 
try:
    x = 5 / 1
    print(x)
except:
    print("Error occurred")



RegX (Regular Expressions)

import re

print(re.match(r'\d+', '123abc'))
print(re.match(r'\w+', 'Hello123'))  # \w+ matches all word characters which include A-Z, a-z, 0-9 and underscore '_' as well
# if we want to print only Hello from Hello123
print(re.match(r'[A-Za-z]+', 'Hello123')) #prints Hello
print(re.match(r'[A-Z]\w+', 'Python3'))
print(re.match(r'[a-z]+', 'abcXYZ'))
print(re.match(r'abc', 'abcde'))
print(re.match(r'^\d', '5days'))
print(re.match(r'.+', 'AnyTextHere'))
print(re.search(r'colou?r', 'The color is nice')) #? is a special character in regx that makes the character just before it optional.
print(re.split(r'\W+', 'Word1,Word2.Word3!')) #output is ['Word1', 'Word2', 'Word3', '']
#if you want to print all the chars from the above line we can use re.findall wich prints ! , and .
print(re.findall(r'\W+', 'Word1,Word2.Word3!'))