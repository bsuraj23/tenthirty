#creating a list of fruits
fruits = ["apple","banana","cherry"]

#printing the entire list
print("Original list:", fruits)

#Accessing elements
print("First fruit:", fruits[0])

#adding a new fruit to the list
fruits.append("orange")
print("List after adding orange:", fruits)

#Removing an item
fruits.remove("banana")
print("List after removing banana:", fruits)

#Iterating through the list
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

