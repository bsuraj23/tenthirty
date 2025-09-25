def count_vowel_consonant(s):
    vowels="AEIOUaeiou"
    vowel_count=0
    consonant_count=0
    for char in s:
        if char.isalpha():  #considers only alphabetic characters
            if char in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    return vowel_count, consonant_count

s="programming language is pyhton"
v,c=count_vowel_consonant(s)
print("Vowels:",v)
print("consonants:",c)

