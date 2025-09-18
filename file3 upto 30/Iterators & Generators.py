#Iterators & Generators
#26.Custom iterator
class Squares:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            val = self.i ** 2
            self.i += 1
            return val
        else:
            raise StopIteration
s = Squares(5)
print(list(s))
#27.Even numbers generator
def even_gen(n):
    for i in range(0, n+1, 2):
        yield i
print(list(even_gen(10)))
#28.Fibannoci generator
def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fib_gen(8)))
#29.Read large file line-by-line (generator)
def file_gen(path):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            yield line
#30.Prime generator
def prime_gen(n):
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
print(list(prime_gen(20)))