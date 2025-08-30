# Basic pdb Debugging Program

import pdb

def add(x, y):
    pdb.set_trace()  # Debugger starts here
    result = x + y
    return result

a = 5
b = 3
print("sum is:", add (a, b))

#Basic pdb Debugging Program

import pdb

def add(x, y):
    pdb.set_trace()  # Debugger starts here
    result = x + y
    return result

a = 5
b = 3
print("Sum is:", add(a, b))

#Debug a Loop

import pdb

for i in range(3):
    pdb.set_trace()
    print("Number:", i)

