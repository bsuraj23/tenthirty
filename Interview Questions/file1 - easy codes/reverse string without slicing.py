#Reverse a string without using slicing
text=input("Enter the string:")
reverse_string=""
for char in text:
    reverse_string=char+reverse_string
print(reverse_string)
