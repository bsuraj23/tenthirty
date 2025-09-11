#Lists, Strings & Collections

#Reverse a list **in place** without using `[::-1]` or `reverse()`
def reverse_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
print(reverse_in_place([1, 2, 3, 4, 5]))


#Write code to flatten a nested list (e.g. `[[1,2],[3,4]] → [1,2,3,4]`).
def flatten_list(nested):
    flat =[]
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat
print(flatten_list([[1,2],[3,4]]))

#Given a string, count the number of vowels and consonants.
def count_vowels_consonants(s):
    vowels= 'aeiouAEIOU'
    v_count = c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

v,c = count_vowels_consonants("Deepthi")
print("Vowels:", v, "Consonants:", c)
    
#To print the fibonacci sequence upto n terms
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        print (a, end='')
        a, b = b, a+b
fibonacci(18)

#to print a multiplication table for a number 
def multiplication_table(num):
    for i in range (1, 11):
        print(f"{num} x {i} = {num * i}")
multiplication_table(15)

#Find all prime numbers upto n
def primes_upto_n(n):
    for num in range(2, n + 1): 
        is_PRIME = True
        for i in range(2, int(num ** 0.5) + 1):  
            if num % i == 0:
                is_PRIME = False
                break
        if is_PRIME:
            print(num, end=' ')
  
primes_upto_n(50)


#check if two strings are Anagrams 
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen","silent"))
print(are_anagrams("hello","world"))

#numbers b/w 1 to 100 that are divisible by both 3 and 5
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')
