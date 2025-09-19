#create and print a tuple 
fruits=("apple", "banana", "cherry")
print("fruits tuple:", fruits)

#access elements by index
names=("archana", "ram", "vilas")
print("first name:", names[0])
print("last name:", names[-1])

#tuple slicing
numbers=(10,20,30,40,50)
print("slice[1:4]:", numbers[1:4])

#tuple unpacking
student=("ravi", 90, "maths")
name,marks,subject=student
print(name,"scored", marks,"in", subject)