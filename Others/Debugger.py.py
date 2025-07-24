import pdb

def calculate_sum(numbers):
    pdb.set_trace()  # Debugger starts here
    total = 0
    for num in numbers:
        total += num
    return total 

my_list = [14, 21, 30]
result = calculate_sum(my_list)
print("Final Result:", result)
