for i in range(1, 6):
    if i == 3:
        continue
    print(i)
#example 2
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)
#example 3
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)
#example 3
text = "Python"
for char in text:
    if char == 'h':
        continue
    print(char)
#example 4
while True:
    word = input("Enter something (type 'quit' to stop): ")
    if word == "quit":
        break
    if word == "skip":
        continue
    print("You entered:", word)
#example 5
for n in range(1, 6):
    if n % 2 == 0:
        continue
    print("Odd number:", n)
