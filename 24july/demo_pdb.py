import pdb
def sq(x):
    return x*x

for i in range(1,5):
    val = sq(i)
    print(f"square of {i} is {val}")
    
    if i==2:
       pdb.set_trace()
       
print("done")
