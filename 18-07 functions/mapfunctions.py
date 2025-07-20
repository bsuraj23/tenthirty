def addition(n):
    return n+n

def mul(n):
    return n*n

number=(1,2,3,4)
result=map(addition,number)
res=map(mul,number)
print(list(result))
print(list(res))