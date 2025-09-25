#Write code to find the frequency of each character in a string.

#mehtod-1

def char_frequency(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq
s="programming"
print(char_frequency(s))


#method-2
from collections import Counter
def char_freq(s):
    return dict(Counter(s))
s="Harish Reddy.Arutla"
text=s.lower()
print(char_freq(text))