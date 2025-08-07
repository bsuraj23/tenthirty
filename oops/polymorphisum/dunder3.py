class List:
    def __init__(self):
        self.data = []
        
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
        
    def __delitem__(self, index):
        del self.data[index]
        
    def __iter__(self):
        return iter(self.data)
    
    def append(self, value):
        self.data.append(value)
        
    def __str__(self):
        return str(self.data)

m= List()
m.append(10)
m.append(20)
m.append(30)

print(m)             # Output: [10, 20, 30]=> using __str__
print(m[1])          #using __getitem__

m[1] = 25            # using __setitem__
print(m)             # Output: [10, 25, 30]

del m[1]             # using __delitem__
print(m)

for i in m:          # using __iter__
    print(i)         # Output: 10, 30