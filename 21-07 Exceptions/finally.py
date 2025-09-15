print("Sample 1")
try:
    number=int(input("Enter the number:"))
except ValueError:
    print("That is not a number")
else:
    print("yes, you entered a good number:", number)
finally:
    print("Program was executed")
    

print("Sample 2")
try:
    number=int(input("Enter the number:"))
except ValueError:
    print("That is not a number")
else:
    print("yes, you entered a good number:", number)
finally:
    print("Thank you for your patience for spending the time in python")