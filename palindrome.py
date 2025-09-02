text = input("Enter a string: ")
reverse =text[::-1]
if text==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
    #palindrome
n=int(input("enter a number: "))
rev=0
original=n
while n>0:
    rem=n%10
    n= n//10
    rev=rev*10+rem
    if original==rev:
        print(original,"is a palindrome")
else:
    print(original,"is not a palindrome")












