def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("racecar"))  
print(is_palindrome("python"))  
#ex 2
def is_palindrome(s):
    result = s.replace(" ", "").lower()
    return result == result[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("zomato"))