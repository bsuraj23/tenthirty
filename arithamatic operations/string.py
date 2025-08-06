#Take input from user
text = input("Enter a string: ")

#Count vowels and consonants
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
 
  for char in text:
        if char in vowels:
            vowel_count += 1
             else:
                consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)


#Reversed the string
reversed_text  = text[::-1]
print("Reversed string:", 
reversed_text)

#Check if palindrome
if  text == reversed_text:
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

