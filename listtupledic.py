my_list=[10,"grape",3.14]
print("list:",my_list)
my_list.append("true")
print(my_list)

my_tuple=(11,"orange",2.71)
print("my_tuple:",my_tuple)
print("my_tuple")

my_dict={"name":"sumanth","age":22,"city":"hyderabad"}
print("my_dict:",my_dict)
my_dict["country"]="usa"
print(my_dict)

print("/niterating over list")
for item in my_list:
    print(item)

print("/niterating over tuple")
for item in my_tuple:
    print(item)

print("/niterating over dictionary")
for item in my_dict:
    print(f"{item}: {my_dict[item]}")
    

