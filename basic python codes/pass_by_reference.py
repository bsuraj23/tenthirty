#pass by reference(behaviour with mutable object)
def modify_list(my_list):
    my_list.append(4)
    print(f"Inside function:{my_list}")
a_list=[1,2,3]
modify_list(a_list)  #function calling
print(f"Outside funtion:{a_list}")