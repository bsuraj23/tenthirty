def fib(n):
    seq=[]
    a, b = 0, 1
    while(len(seq) < n):
        seq.append(a)
        a, b = b, a + b
    return seq
print(fib(10))
print(fib(5))  # For better readability in output 
        