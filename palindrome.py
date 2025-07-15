n=int(input("Enter the number:"))
rev=0
original=n
while n>0:
    rem=n%10
    n=n//10
    rev=rev*10+rem
if original == rev:
    print(original,"is a Palindrome")
else:
    print(original,"is not a palindrome")
