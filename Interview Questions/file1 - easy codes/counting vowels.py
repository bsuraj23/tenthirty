# Count vowels in a string
#using for loop
def vowel_count(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:
            count+=1
    return count

text="harishreddy"
print(vowel_count(text))


#using list comprehension
text="A python Programming"
count=sum(1 for char in text if char.lower() in "aeiou")
print(count)



