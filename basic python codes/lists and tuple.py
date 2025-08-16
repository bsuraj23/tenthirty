#lists
#lists
fruits = ["apple", "banana", "Orange", "mango"]
print(fruits)
print("First fruit",fruits[0])
print("last fruit",fruits[-2])
fruits[1] = "cherry"
print(fruits)
fruits.append("papaya")     #appending at last
fruits.insert(1,"grape")   #inserting by index
fruits.extend(["guvava","pine"]) #extending multiple items
print(fruits)
fruits.pop(2)      #poping one element
fruits.remove("papaya")  #removing one element
print(fruits)     
del fruits[1:3]    #deleting multiple items
print(fruits)
fruits.sort()     #sorting by alphbetical order
print(fruits)
fruits.reverse()       #reversing
print(fruits)
fruits.clear()     #clearing the list
print(fruits)




#tuples
info = ("Harish", 21, "B Tech", True)
print(info)
print(info.count("B Tech"))
