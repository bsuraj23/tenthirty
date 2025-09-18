#Create a set and print elements
colors={"red", "green", "blue"}
print("Set:", colors)

#Add an element to a set
fruits={"apple", "banana"}
fruits.add("cherry")
print(fruits)

#Remove an element from a set
fruits={"grapes", "mango", "guava"}
fruits.remove("mango")
print(fruits)

#Check if element exists in a set
numbers={1,2,3,4}
if 3 in numbers:
   print("3 is present")

#Union of two sets
a={1,2,3}
b={3,4,5}
print("Union:", a.union(b))

#Intersection of two sets
a={1,2,3}
b={2,3,4}
print("Intersection:", a.intersection(b))

#Difference a between sets
a={1,2,3,4}
b={3,4,5}
print("Difference (a-b):", a.difference(b))

#Symmetric difference(not common elements)
a={1,2,3}
b={3,4,5}
print("Symmetric Difference:", a.symmetric_difference(b))

#Loop through a set
animals={"dog", "cat", "rabbit"}
for animal in animals:
    print(animal)

#Clear a set
letters={"a", "b", "c"}
letters.clear()
print("Cleared set:", letters)

