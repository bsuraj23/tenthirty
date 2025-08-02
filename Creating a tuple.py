# Creating a tuple
fruits=("apple", "banana", "cherry", "orange")

#Printing the entire tuple
print("Fruits Tuple:", fruits)

#Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

#Iterating through the tuple
print("All fruits:")
for fruit in fruits:
    print(fruit)

#Checking length
print("Total number of fruits:", len(fruits))

#Tuple with mixed data types
mixed_tuple=(101, "Ammu", 75.5)
print("Mixed Tuple:", mixed_tuple)

#Tryingg to change a value (will raise error)
try:
    fruits[1]="grape"
except TypeError as e:
    print("Error:", e)