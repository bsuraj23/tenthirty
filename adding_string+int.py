def add_string_number(text,number):
    if text.isdigit():
        return int(text)+number
    else:
        return "Error: The string is not a number"
print(add_string_number("100",50))