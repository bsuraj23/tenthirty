try:
    number=int(input("Enter the number:"))
except ValueError:
    print("That is not a number")
else:
    print("yes, you entered a good number:", number)