for i in range(1, 6):
    if i == 2:
        print("pass executed at", i)
        pass  # does nothing, placeholder
    elif i == 3:
        print("continue executed at", i)
        continue  # skips current iteration
    elif i == 5:
        print("break executed at", i)
        break  # exits the loop
    print("Looping number:", i)
