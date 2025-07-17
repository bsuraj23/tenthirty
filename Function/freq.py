def freq(txt):
    words=txt.lower().replace(',', '').replace('.', '').split()
    freq={}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
txt="Hello world ,hello is a world"
print(freq(txt))