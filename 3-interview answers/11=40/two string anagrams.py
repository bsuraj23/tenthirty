#Implement a function to check if two strings are anagrams.

def are_anagrams(str1, str2):
    # Normalize: remove spaces & lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare character counts
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    
    # Count characters in str1
    for ch in str1:
        char_count[ch] = char_count.get(ch, 0) + 1
    
    # Subtract counts using str2
    for ch in str2:
        if ch not in char_count:
            return False
        char_count[ch] -= 1
        if char_count[ch] < 0:
            return False
    
    return True

# Example usage
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("✅ The strings are anagrams.")
else:
    print("❌ The strings are not anagrams.")
