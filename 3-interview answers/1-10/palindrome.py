def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:  # compare characters
            return False
        left += 1   # move forward
        right -= 1  # move backward
    
    return True

# Example usage
print(is_palindrome("madam"))   # True
print(is_palindrome("python"))  # False
