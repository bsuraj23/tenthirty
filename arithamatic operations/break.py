#This program asks for numbers and stops when the user enters 0
while True:
    number = int(input("Enter a number(0 to stop):"))
    if number == 0:
        print("Loop stopped because you entered 0.")
        break
    print(f"You entered: {number}")