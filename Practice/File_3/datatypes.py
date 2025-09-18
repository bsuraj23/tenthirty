#Data types & Variables
#String is Palindrome or not (without using slicing)
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome("radar"))

#Given a list of numbers, remove all duplicates (without using set())
def remove_duplicates(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

user_input = input("Enter numbers separated by spaces: ")
number_list = [int(x) for x in user_input.split()]

result = remove_duplicates(number_list)
print("List after removing duplicates:", result)


#function to merge two dictionaries.
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  
    for key, value in dict2.items():
        merged[key] = value  
    return merged

dict_a = {"name": "Deepthi", "course": "AI"}
dict_b = {"course": "Full Stack", "location": "Hyderabad"}

result = merge_dicts(dict_a, dict_b)
print("Merged Dictionary:", result)

#Write code to find the frequency of each character in a string.
s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

#Implement your own version of `max()` without using the built-in function.
numbers = input("Enter numbers separated by space: ")
num_list = [int(n) for n in numbers.split()]
max_num = num_list[0]
for n in num_list:
    if n > max_num:
        max_num = n
print("The biggest number is:", max_num)