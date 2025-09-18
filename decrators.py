class fibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count <self.n:
            self.count +=1
            value = self.a
            self.a, self.b = self.b, self.a +self.b
            return value
        else:
            raise StopIteration
        
for num in fibonacciIterator(10):
    print(num, end=" ")  