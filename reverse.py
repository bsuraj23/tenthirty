def reverse(s):
    result = "".join(reversed(s))
    return(result)

print(reverse("hello"))
# #ex 2
test = "rahul"
print(test[::-1])

# #ex3

s="harish"
a=""
for char in s:
    a=char+a
print(a)