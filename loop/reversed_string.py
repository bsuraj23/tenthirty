s="Manish"
rev=""

#starting from the last character of the string
n=len(s)-1 

while n >=0:
    rev += s[n] #apending characters in reverse order
    n -=1       #decresing index

print(rev)

#without any built-in functions
# s = "Manish"
# rev = ""
# for char in s:
#     rev = char + rev
# print("Reversed string:", rev) 