#pass by value(behaviour with immutable objects)
def modify_number(num):
    num+=50
    print(f"Inside function:{num}")
x=4
modify_number(x)
print(f"Outside function:{x}")