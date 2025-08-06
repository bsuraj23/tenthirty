# list without using lambda
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_list = list(map(square, numbers))
print("Original list:", numbers)
print("Squared list:", squared_list)
