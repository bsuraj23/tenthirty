 
# **Coding Practice:**

# Q1 Reverse a string without using slicing.?

def reverse_string(s):

    result = ""
    for char in s:
        result = char + result
    return result
print(reverse_string("MR.SUNIL"))  # Output: "olleh"

# 2Q Find the largest number in a list.

list = [1,3,4,5,6,10]
largest = max(list)
print(largest) 


# 2Q Count vowels in a string.?
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("MR.SUNIL"))  


# 4Q Write a program to check if a number is prime ?

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
       return True
   
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False
 
 