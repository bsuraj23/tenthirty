
# Program to odd numbers

for i in range(1,100,2):
    print(i)

# Program to even numbers

for i in range(0,101,2):
    print(i)



# Prime number less than n

n = int(input("Enter a number: "))

for num in range(2, n):  
    is_prime = True
    for i in range(2,n):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')