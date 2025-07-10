n=input("Enter a string: ")
if n.isalpha():
    print("The string is alphabetic")
elif n.isdigit():
    print("The string is numeric")
elif n.isalnum():
    print("The string is alphanumeric")
elif n.isspace():
    print("The string contains only whitespace")
else:
    print("The string contains special characters or is empty")
    