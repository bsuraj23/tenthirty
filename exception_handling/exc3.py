a=10
try:
    lst=[1, 2, 3]
    print(lst[2])
    num=int(input("Enter a number: "))
    c=a/num
    print("Result:", c)
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Index out of range")
