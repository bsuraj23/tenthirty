count = 0  # global variable

def increment_global():
    global count
    count += 1
    print("Inside function, count =", count)

increment_global()
increment_global()
print("In global scope, count =", count)
