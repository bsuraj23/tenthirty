list1 =[1, 2, 1]
list2 =[1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

if copy_list1 == list1:
    print(" palindrome")
elif copy_list2 == list2:
    print("not palindrome") 
 