#create set
my_set = {1, 2, 3, 4}
print("Set:", my_set)

#add element in set
my_set = {1, 2, 3}
my_set.add(4)
print("After adding 4:", my_set)

#remove element from set
my_set = {1, 2, 3, 4}
my_set.remove(3)
print("After removing 3:", my_set)

#discard element from set
my_set = {1, 2, 3}
my_set.discard(3)  # No error if 5 is not in the set
print("After discard:", my_set)

#check if element exists in set
my_set = {"apple", "banana", "cherry"}
if "banana" in my_set:
    print("banana is in the set")

#set union in set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

#set intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

#set difference
set1 = {1, 2, 3, 4}
set2 = {3, 4}
difference_set = set1.difference(set2)
print("Difference:", difference_set)

