try:
    int("xyz")
except Exception as e:
    print("Caught Exception:", e)


try:
    num = 20
except:
    print("Error occurred")
else:
    print("No exception, num is", num)
    

try:
    x = int(input("Enter number: "))
except:
    print("Invalid input")
finally:                        #here this finally code will execute compulsary if the try or except works or doesnt
    print("Execution finished")    #works it dont care