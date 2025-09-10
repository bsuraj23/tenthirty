fruits=["apple", "banana", "carrot"]
print(fruits)
print(fruits[0])
print(fruits[-1])
fruits.append("mango")
fruits.remove("banana")
print(fruits)
#loop through list
for fruit in fruits:
    print(fruit)
#list squares of number
numbers=[1,2,3,4]
squares=[n**2 for n in numbers]
print(squares)
#largest numbers
numbers=[10,4,6,98,34]
print(max(numbers))
#reverse list
numbers.reverse()
print(numbers)
#remove duplicates
numbers=[1,2,3,3,4,4,5]
unique_numbers=list(set(numbers))
print(unique_numbers)
#sort list by second element of tupe
pairs=[(1,2), (2,3), (5,2)]
pairs.sort(key=lambda x:x[1])
print(pairs)