# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#    print(" "*(n-i) + "* "*i )
i=1
n = int(input("Enter a number: "))
while n >= i:
    print(" " * (n - i) + (2 * i - 1) * "*")
    i += 1
    
i=n-1    
while i >=1:
    print(" " * (n - i) + (2 * i - 1) * "*")
    i -= 1

# for i in range(1, n + 1):
#     print(" " * (n - i) + (2* i - 1) * "*")
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + (2 * i - 1) * "*")
