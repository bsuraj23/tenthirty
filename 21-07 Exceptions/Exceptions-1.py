try:
    print(10/0)    #if this print statement is false or not executed it goes to except function and it print exception code
except ZeroDivisionError:
    print("Division")
except ConnectionAbortedError:
    print("Connection problem")

try:
    print(int("Harish"))  #here string is not integer so it cant print, it goes into except code what ever the error occurs
except ValueError:
    print("Invalid Number")

print("printing 3rd")
a=10
try:
    list=[1,2,3,4]
    print(list[3])
    num=int(input("Please enter an integer:"))
    c=a/num
    print(c)
except IndexError:
    print("Index out of range")


print("Printing 4th")
try:
    d={'a':1}
    print(d['a'])
    print("iam after line 3")  #if this try statement doesnot work, whatever the error shows it goes to exception statement
except IndexError:
    print("Index out of range")
except ZeroDivisionError:
    print("division by zero error")
except KeyError:
    print("key not found")
