#custom iterator for fobonacci numbers  
class fib:
    def __init__(self,n):
        self.n=n 
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n<=0:
            raise StopIteration
        self.n-=1
        val=self.a
        self.a,self.b=self.b,self.a+self.b
        return val
for x in fib(6):
        print(x)


