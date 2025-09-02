for i in range(1,16):
    print(i)

#print each chacter in string
text="hello"
for i in text:
    print(i)

#sum of numbers from 1 to n using while loop
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Sum:", sum)

#even numbers 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#finite loop with break
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input == "exit":
        break
    print("You entered:", user_input)

#loop with continue
for i in range(1, 6):
    if i == 3:
        continue  # skip 3
    print(i)
    #nested loop multiplication table
    for i in range(1, 4):  # rows
        for j in range(1, 4):  # columns
            print(i * j, end=' ')
            print()
#count 1 to 5
for i in range(5, 0, -1):
    print(i)

    



