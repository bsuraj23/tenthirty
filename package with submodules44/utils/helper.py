#44.Create a package with submodules and demonstrate relative imports
def greet(name):
    return f"Hello, {name}!"

def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1]
