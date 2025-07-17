def prime(n):
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            return
    print(f"{n} is a prime number")
prime(62)
prime(3)
prime(4)
prime(5)