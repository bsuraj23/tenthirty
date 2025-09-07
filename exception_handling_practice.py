#Basic try–except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter an integer.")
#Multiple except blocks
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
#Using finally
try:
    f = open("example.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution finished (finally block always runs).")
#Try–except–else
try:
    num = int(input("Enter a positive number:"))
except ValueError:
    print("Error:That's not a valid number!")
else:
    print("Great! You entered:", num)    
#Raising exceptions manually
def check_age(age):
    if age < 18:
        print("Error:It should be 18 or above 18")
    else:
        print("Eligible to vote!")
try:
    check_age(20)
except ValueError as e: #e:exception message
    print("Error:", e)
#Custom exception class
class NegativetypeError():
    pass
def square_root(num):
   if num < 0:
      print("Negative number is not applicable!")
   return num ** 0.5
try:
    print(square_root(22))
except ValueError as e:   
    print("Error:",e)   