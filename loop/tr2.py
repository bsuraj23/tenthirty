# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#    print(" "*(n-i) + "* "*i )

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print(" " * (n - i) + (2* i - 1) * "*")
    
n=5
i=1
while n >=i:
    print(" " * (n - i) + (2 * i - 1) * "*")
    i += 1