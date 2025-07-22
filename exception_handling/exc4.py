try:
    d={"a": 1, "b": 2}
    print(d["1"])
    #to check if it prints the next line
    print("This line will not execute if KeyError occurs")
except KeyError:
    print("Key not found in dictionary")
except TypeError:
    print("Type error occurred")