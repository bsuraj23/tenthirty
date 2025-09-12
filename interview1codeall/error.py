#Count word frequencies in a file.
with open('file.txt') as f:
    words = f.read().split()
freq = {w: words.count(w) for w in set(words)}
print(freq)

#Context manager for file operations
class File:
    def __init__(self,name,mode):
        self.name=name; self.mode=mode
    def __enter__(self):
        self.f=open(self.name,self.mode)
        return self.f
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.f.close()
with File('test.txt','w') as f:
    f.write('hello')

#Squares of even numbers using map & filter.
nums=[1,2,3,4,5,6]
evens=filter(lambda x:x%2==0,nums)
squares=list(map(lambda x:x*x,evens))
print(squares)
