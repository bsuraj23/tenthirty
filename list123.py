fruits=["apple", "banana", "cherry"]
print("Fruits list:", fruits)


colors=["red", "green", "blue"]
colors.remove("green")
del colors[2]
print("After removing:", colors)

names=["archana", "vilas","rithu", "priya"]
print("first two names:", names[:2])
for name in names:
    print("Hello", name)