def my_decorator(fun):
    def wrapper():
        print("before the function runs")
        fun()
        print("After the function run")
    return wrapper
@my_decorator   #this is the decorator to hello()
def hello():
    print("Helo world!")
hello()

#decorator with argument
def smart_division(fun):
    def wrapper(a,b):
        print(f'Division {a} by {b}')
        if b==0:
            return "Error!, Division by zero"
        return fun(a,b)
    return wrapper
@smart_division
def division(a,b):
    return a/b
print(division(5,0))
print(division(10,5))

