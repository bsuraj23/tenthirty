try:
    int("acn")
except ValueError:
    print("Cannot assign a string to an integer variable")
except ZeroDivisionError:
    print("Cannot divide by zero")