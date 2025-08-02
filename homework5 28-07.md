#Write down a function which takes String,Integer and returns the addition of it

In Python, if you want to write a function that takes a string and an integer, converts the string to an integer, and returns their sum, here’s a simple function:

def add_string_and_int(s, num):
    try:
        s_int = int(s)  
        return s_int + num
    except ValueError:
        return "Error: The string does not contain a valid integer."
Example usage:

result = add_string_and_int("10", 5)
print(result) 

result = add_string_and_int("abc", 5)
print(result) 