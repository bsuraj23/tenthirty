import pdb  #Import the debugger

def add_numbers(a, b):
    pdb.set_trace()  #Pause the code here and helps us know what is happening
    result = a + b
    return result
x = 5
y = 10
total = add_numbers(x, y)
print("Total:", total)

#When we run the file, it will pause at pdb.set_trace()
#and in the terminal we can see 
# => result = a+b
#    (Pdb)
