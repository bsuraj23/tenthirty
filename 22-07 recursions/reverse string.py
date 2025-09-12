#recursion
def reverse_string(text):
    if len(text)==0:
        return ""
    return reverse_string(text[1:])+text[0]
print(reverse_string("Harish"))

#slicing
def reverse_string(text):
    return text[::-1]
print(reverse_string("Reddy"))