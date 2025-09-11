s="sashi kiran"
reversed_s= " "
for i in s:
    reversed_s = i + reversed_s
print(reversed_s)

#largest number
list = [10, 5, 8, 2, 15]
large=list[0]
for i in list:
    if i > large:
        large = i
        print("Largest number is:", large)

#checking wheather number is prime or not
num = 23
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")