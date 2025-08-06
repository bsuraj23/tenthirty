def reverse_string(s):
    if len(s)==0:
        return None
    return reverse_string(s[1:])+s[0]
print(reverse_string("/.;"))
