#HOF(higher order function) -it is a simple function but it takes another function as an argument
def power(n):
    def exponent(x):
        return x**n
    return exponent

square=power(2)
cube=power(3)

print(square(5))    #25
print(cube(3))      #27