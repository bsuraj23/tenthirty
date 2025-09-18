

# Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=' ')


# Print odd numbers from 1 to 20
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=' ')

 
# Print prime numbers from 1 to 50
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
# Examples of for Loop in Python
# Example 1: Print numbers 1 to 5

for i in range(1, 6):
    print(i)
# Example 2: Loop through a list

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
