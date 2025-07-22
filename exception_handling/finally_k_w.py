try:
    x=int(input("Enter a number: "))
except:
    print("Invalid input, please enter a valid integer.")
finally:
    print("Execution completed, regardless of error.")