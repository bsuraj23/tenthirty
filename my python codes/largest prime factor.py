def problem3(n=600851475143):
    factor=2
    while n>1:
        if n%factor==0:
            n//=factor
        else:
            factor+=1
    return factor

print(problem3())