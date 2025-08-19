import re


print(re.match(r'\d+', '1abc')) # it is searching numbers it takes from starting no's
print(re.match(r'\w+', 's##$')) # It look for all letters and no's from start
print(re.match(r'[A-Z]\w+', 'Python3'))#it searches for one big capital 
print(re.match(r'[a-z]+', 'abcXYZ'))#it look for one or more small letter
print(re.match(r'abc', 'abcde')) #it look for abc from starting
# ^ it means starting of word and \d mean one number
print(re.match(r'^\d', '5days5'))
# '.' mean anyletter or num or symbol '+' one more time 
print(re.match(r'.+', 'AnyTextHre'))

#print(re.match(r'\w','ello'))

m = 90
n = "hello this is raj from andhra"
print(re.match(r'hello',n))
