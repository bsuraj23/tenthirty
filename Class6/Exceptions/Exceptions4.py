try:
    d = {"a": 1}
    print(d["g"])
    print("I amm after line 3 ")

except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("Division by zero error")
except KeyError:
    print("Key notdkfadhdfgdfhg found")
