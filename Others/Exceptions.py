try:
    print(10/0)  
except ZeroDivisionError:
    print("Division")
except ConnectionAbortedError:
    print("Connection problem")

try:
    print(int("Mr.Sunil"))
except ValueError:
    print("Invalid Number")