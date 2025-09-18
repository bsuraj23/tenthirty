#Implement a module with a helper function `is_palindrome()`, then import and test it.
# test_palindrome.py

from string_utils import is_palindrome

words = ["level", "Racecar", "hello", "A man a plan a canal Panama"]

for word in words:
    if is_palindrome(word):
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is not a palindrome")
