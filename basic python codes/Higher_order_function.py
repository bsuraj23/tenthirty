#HOF(higher order function) -it is a simple function but it takes another function as an argument
def power(n):
    def exponent(x):
        return x**n
    return exponent

square=power(2)
cube=power(3)

print(square(5))    #25
print(cube(3))      #27

#built-in-higher order functions
nums = [1, 2, 3, 4, 5]
# double each number
print(list(map(lambda x: x*2, nums)))
# keep even numbers
print(list(filter(lambda x: x%2==0, nums)))
