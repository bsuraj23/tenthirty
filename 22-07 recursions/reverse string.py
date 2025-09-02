#without RecursionError
def reverse_string(s):
    return s[::-1]
print(reverse_string("harish"))


#recursion
def reverse_string(s):
    if len(s)==0:
        return ""
    return reverse_string(s[1:])+s[0]

print(reverse_string("Harish"))


