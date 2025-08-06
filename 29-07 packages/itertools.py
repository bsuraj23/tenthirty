import itertools

for i in itertools.islice(itertools.count(1),10):
    print(i)


#cycle through list
cyc=itertools.cycle([1,2,3,4,5])
print(next(cyc),next(cyc),next(cyc),next(cyc),next(cyc),next(cyc))

#combinations
print(list(itertools.combinations('ABCD',3)))