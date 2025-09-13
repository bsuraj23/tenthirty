#Control Flow and Loops
#11.Fibanocci upto n terms
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print() 
#12.Multiplication table(1 to 10)
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")
table(21)
#13.Prime numbers upto n
def primes(n):
    res = []
    for num in range(2, n+1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            res.append(num)
    return res
print(primes(20))
#14.Anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print()  
#15.Number divisible by 3 and 5
[x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print([x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0])