def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

input_str = "Hello, Python World!"
print(count_vowels(input_str))

