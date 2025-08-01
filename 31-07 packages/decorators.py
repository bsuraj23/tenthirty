def my_decorator(fun):
    def wrapper():
        print("Before fun runs")
        fun()
        print("After fun runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
say_hello()