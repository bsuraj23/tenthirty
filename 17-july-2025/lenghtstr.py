import time
Name = input("Enter your name:\n")

counter = 0

for letter in Name:
    counter += 1

time.sleep(2)
print("Length of the string:",counter)
