# Write a function to check if a string is a palindrome without using slicing.
def is_palindrome(word:str)->bool:
    left,right=0,len(word)-1
    while left<right:
        if word[left] != word[right]:
            return False
        left=left+1
        right=right-1
    return True
print(is_palindrome("harisirah"))
print(is_palindrome("madam"))
print(is_palindrome("Harish"))
