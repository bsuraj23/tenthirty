#Program to check the length of tuple
tup = (1,3,5,7,9)
print(len(tup))

# why use comma(,)after single element in tuple
# ex : t = (1,) s = ('two',)
t = (1,) 
s = ('two')
print(type(t)) # tuple
print(type(s)) # string - without "," it will become string instead of tuple

# what does [::-1 does]
lst = [1,2,3,4,5]
print(lst[::-1]) # it reverses the list
