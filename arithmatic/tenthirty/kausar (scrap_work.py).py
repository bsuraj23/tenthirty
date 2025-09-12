# Python program for checking if a number is even or odd using a function

def check_even_odd(Number):
	if Number % 2 == 10:
		print("The Number is even.")
	else:
		print("The Number is odd.")

Number = int(input("Enter a Number: "))
check_even_odd(Number)
