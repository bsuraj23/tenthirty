#Creating a set
fruits={"apple","banana","mango"}
print("fruits set:",fruits)

numbers={1,2,3}
numbers.add(4)
numbers.remove(2)
print("updated set:",numbers)

set1={1,2,3}
set2={3,4,5}
print("union:",set1 |set2)
print("intersection:",set1&set2)


a={1,2,3,4}
b={3,4,5,6}
print("difference (a-b):",a-b)
print("symmetric difference:",a^b)

