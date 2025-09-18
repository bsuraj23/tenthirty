#43.Write code using `__name__ == "__main__"` to run tests only when executed directly.

def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome("Racecar"))  # True
    print(is_palindrome("Hello"))    # False
