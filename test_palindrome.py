#42 test_palindrome.py

from helpers import is_palindrome

if __name__ == "__main__":
    test_strings = ["Racecar", "Hello", "A man a plan a canal Panama", "No lemon, no melon"]
    
    for text in test_strings:
        result = is_palindrome(text)
        print(f"'{text}' -> Palindrome? {result}")
