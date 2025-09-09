# Reverse a string ( Without Slicing)
s = "Deepthi"
result = ""
for ch in s:
    result = ch + result
print(result)


#Find the largest number in a list.
numbers = [12, 45, 78, 34, 89, 23]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("The largest number is:", largest)


# Count vowels in a string
v = "Deepthi"
vowels = "aeiouAEIOU"
count = 0
for ch in v:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)


#Write a program to check if a number is prime
num = int(input("Enter a number: "))
if num < 2:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")