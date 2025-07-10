
#adding an element at first place 
#meth1
list = [2,3,5]
list.insert(0,1)
print(list)

#method 2
my_list = [20,30,40]
my_list = [10] + my_list
print(my_list)

#method 3
our_list = [200,300,400]
our_list = [100, *our_list]
print(our_list)
