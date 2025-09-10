#add
import operator

# Adding two numbers
a = 10
b = 20
result = operator.add(a, b)

print("Addition of", a, "and", b, "is:", result)


#any
values = [0, True, None, 5]
result = any(values)
print("Any ture?", result)

#all
values = [1, False, 5]
result = all(values)
print("All true?", result)