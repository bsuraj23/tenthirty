n=int(input("Enter no.:"))
rem=0
temp=0
rev=n
while n > 0:
    rem=n%10
    temp=temp*10+rem
    n=n//10

if rev==temp:
    print("Pali")
else:
    print("NP")
    