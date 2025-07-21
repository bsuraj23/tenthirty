try:
    int("xyz")
except Exception as e:
    print("Caught Exception:", e)


try:
    num = 10
except:
    print("Error occurred")
else:
    print("No exception, num is", num)
    

try:
    x = int(input("Enter number: "))
except:
    print("Invalid input")
finally:
    print("Execution finished")