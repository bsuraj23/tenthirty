def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():               # check only alphabetic characters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Example usage
s = "swathi"
v, c = count_vowels_consonants(s)
print("Vowels:", v)        
print("Consonants:", c)    
