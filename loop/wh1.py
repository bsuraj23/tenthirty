# n= int(input("Enter a number: "))
# rem=0
# temp=n
# while n > 0:
#     rem = rem * 10 
#     rem+= n % 10
#     n = n // 10
# if temp == rem:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

n = int(input("Enter a number: "))
a=1
b=2
while n > 0:
    c=a+b
    a=b
    b=c
    n-=1
    print(c)