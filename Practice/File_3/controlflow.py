#Control Flow & Loops

#Print the fibonacci sequence upto n terms
n = 10  
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Multiplication table for a number
num = 7  
print(f"Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#FInd all prime numbers upto n
n = 50
print("Prime numbers up to", n, ":")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

#function to check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "silent"))  
print(are_anagrams("hello", "world"))   

#Find all numbers between 1 and 100 divisible by both 3 and 5
print("Numbers divisible by both 3 and 5:")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")