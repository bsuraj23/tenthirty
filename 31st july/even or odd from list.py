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



#output:

#How many numbers do you want to enter? 6
#Enter number 1: 56
#Enter number 2: 78
#Enter number 3: 65
#Enter number 4: 88
#Enter number 5: 566
#Enter number 6: 9876
#[56, 78, 65, 88, 566, 9876]
#56 is Even
#78 is Even
#65 is Odd
#88 is Even
#566 is Even
#9876 is Even        
