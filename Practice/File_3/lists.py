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

#Find the second largest number in a list

numbers = [10, 20, 4, 45, 99, 99]
unique_numbers = list(set(numbers))   
unique_numbers.sort()                 
print("Second largest number is:", unique_numbers[-2])

#Rotate a list by k elements (Circular shift)
def rotate_list(lst, k):
    k = k % len(lst)  
    return lst[-k:] + lst[:-k]
numbers = [1, 2, 3, 4, 5]
k = 2
rotated = rotate_list(numbers, k)
print("Rotated list:", rotated)  
