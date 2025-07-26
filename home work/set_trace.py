# Basic pdb Debugging Program
import pdb

def calculate_sum(a, b):
    pdb.set_trace()
    result = a + b
    return result

    x = 5
    y = 10
    total = calculate_sum(x, y)
    print("Total:", total) 
