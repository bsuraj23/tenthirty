
                 # Python program for checking if a number is even or odd using a function

def check_even_odd(number):
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

number = int(input("Enter a number: "))
check_even_odd(number)