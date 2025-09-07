class Person:
    pass

p = Person()

setattr(p, 'name', 'Rizwan')
setattr(p, 'age', 21)
setattr(p, 'country', 'India')
setattr(p, 'status', True)
setattr(p, 'score', 99)

print(getattr(p, 'name'))
print(getattr(p, 'age'))
print(getattr(p, 'country'))
print(getattr(p, 'status'))
print(getattr(p, 'score'))

# delattr()
delattr(p,'score')  
setattr(p, 'score', 95)

print(getattr(p, 'status')) 
print(getattr(p, 'score'))