#printing only vowels from a string
text = "hello world"
vowels = "aeiouAEIOU"

for char in text :
    if char in vowels :
        print(char) 
        
text = "education"
vowels = "aeiou"
printed = []
print()
for char in text:
    if char in vowels and char not in printed:
        print(char)
        printed.append(char) 

#store all vowels in a list 
text = "hello how are you"
vowel_list = [char for char in text if char in "aeiouAEIOU"]
print(vowel_list)

#count the number of vowels in astring
text = "python is a programming language"
vowel_count = sum(1 for char in text if char in "aeiouAEIOU")
print(f"number of vowels in string: {vowel_count}")
