#Lambda function to print user input

# Take user input
user_input = input("Enter something: ")

# Lambda function to print input
print_input = lambda x: print("You entered:", x)

# Call the lambda
print_input(user_input)