class FibonacciIterator:
    def __init__(self,limit):
        self.limit=limit
        self.a,self.b=0,1
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        value = self.a
        self.a,self.b=self.b,self.a+self.b
        self.count += 1
        return value

for num in FibonacciIterator(10):
    print(num)