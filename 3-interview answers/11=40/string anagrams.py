#Implement a function to check if two strings are anagrams.
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare sorted characters
    return sorted(str1) == sorted(str2)

# Example usage
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("✅ The strings are anagrams.")
else:
    print("❌ The strings are not anagrams.")
