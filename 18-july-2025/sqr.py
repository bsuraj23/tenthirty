#write a code for sqrt using input 
import math
def square(number):
    result = math.sqrt(number)
    return result

number = int(input("Enter your number"))
answer = square(number)

print(f"The square of {number} is {answer} ")