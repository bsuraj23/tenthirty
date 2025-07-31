# Lambda function to return user input
a = lambda x: x
user_input = input("Enter something: ")
print("You entered:", a(user_input))

#Square number without using lambda function
n = [1, 2, 3, 4, 5]
squared = []
for i in n:
    squared.append(i ** 2)
print("Squared list:", squared)

#To print even numbers from a list without using lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
for i in numbers:
    if i % 2 == 0:
        print(i)


