
import re
# t = "hello"
# #this will search whole sentence 
# print(re.search(r'hello',t))
# # this $ mean we need to give an end
# print(re.search(r'end$',"this is an end"))
# s="mani@end"
# print(re.search(r'^\w+',s))

#m = "this is a good siva"
# #?- this means optional for that word 
# print(re.search(r"sh?iva",m))
# #search of space
# print(re.search(r'\s',m))

# pattern = re.compile(r'.+') # anything will accept even space also
# print(pattern.search("helloo"))
# print(pattern.search(""))


#split removes the given one
n = "hello this is mani no_-----!#@!1,:23"
# print(re.split(r'\s',n))
# print(re.split(r'\d+',n))

# print(re.split(r'[:,]',n))

# print(re.split(r'-',n))

#fullmatch

print(re.fullmatch(r'\w+',n))