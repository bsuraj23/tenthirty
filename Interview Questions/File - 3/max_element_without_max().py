#Implement your own version of max() without using the built-in function.

#method-1 without max()
def my_max(numbers):
    max=numbers[0]
    for num in numbers[1:]:
        if num>max:
            max=num
    return max
print(my_max([1,2,3,4,5,6,7,4,7,2,9,32]))

#method-2  with max()
print(max(1,2,3,2,4,6,5,9,2,89,34,534,4,98,341))

