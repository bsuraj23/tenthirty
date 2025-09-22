from collections import Counter
tuple=(1,2,4,5,32,7,9,3,5,7,8,36)
frequencies=Counter(tuple)
print(frequencies)

#normal method
tup=(1,2,4,5,32,7,9,3,5,7,8,36)
freqs={}
for item in tup:
    if item in freqs:
        freqs[item]+=1
    else:
        freqs[item]=1

print(freqs)


