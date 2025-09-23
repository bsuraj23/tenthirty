
#without recursion
def summing(n):
    total=0
    for i in range(0,n+1):
        total=total+i
    return total
print(summing(10))


#Recursion
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(10))