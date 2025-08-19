# num = list(input())
# # for i in num:
# #     if i % 2 == 0:
# #         print("even numbers are:",i)
# #     else:
# #         print()
# print(num)

# Take input list from the user
# Ask how many numbers will be in the list


n = int(input("How many numbers do you want to enter? "))

# Create an empty list
numbers = []

# Take input one by one and add to the list
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(numbers)
# Check and print if each number is even or odd
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")
