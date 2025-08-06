# s="Manish"
# rev=""

# #starting from the last character of the string
# n=len(s)-1 

# while n >=0:
#     rev += s[n] #apending characters in reverse order
#     n -=1       #decresing index

# print(rev)

#without any built-in functions
s =input("Enter a string: ")
a=s.lower()
rev = ""
for i in a:
    rev = i + rev
print("Reversed string:", rev) 

if a == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")