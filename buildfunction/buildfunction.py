# Example: Build Functions in Python

def greet_user(name):
    return f"Hello, {name}! 👋"

def add_numbers(a, b):
    return a + b

def build_sentence(word_list):
    return " ".join(word_list).capitalize() + "."

# Using the functions
user_name = "Alex"
numbers = (5, 7)
words = ["python", "is", "fun"]

print(greet_user(user_name))
print(f"The sum is: {add_numbers(*numbers)}")
print(f"Sentence: {build_sentence(words)}")
