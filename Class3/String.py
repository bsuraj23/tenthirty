var1 = 'Hello World!'
var2 = "Python Programming"
print(var1)

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
print ("My name is %s and weight is %d kg!" % ('Zara', 21) )


#changing content in String object

var1 = 'Hello World!'


#we can change its content by reassiging


#capitalize()
#Capitalizes first letter of string
#2	center(width, fillchar)
#Returns a space-padded string with the original string centered to a total of width columns
#3	count(str, beg= 0,end=len(string))
#Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given
#4	decode(encoding='UTF-8',errors='strict')
#Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.
5	encode(encoding='UTF-8',errors='strict')
Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.
6	endswith(suffix, beg=0, end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise
7	expandtabs(tabsize=8)
Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided
8	find(str, beg=0 end=len(string))
Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise
9	index(str, beg=0, end=len(string))
Same as find(), but raises an exception if str not found
10	isalnum()
Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise
11	isalpha()
Returns true if string has at least 1 character and all characters are alphabetic and false otherwise
12	isdigit()
Returns true if string contains only digits and false otherwise
13	islower()
Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise
14	isnumeric()
Returns true if a unicode string contains only numeric characters and false otherwise
15	isspace()
Returns true if string contains only whitespace characters and false otherwise
16	istitle()
Returns true if string is properly "titlecased" and false otherwise
17	isupper()
Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise
18	join(seq)
Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string
19	len(string)
Returns the length of the string
20	ljust(width[, fillchar])
Returns a space-padded string with the original string left-justified to a total of width columns
21	lower()
Converts all uppercase letters in string to lowercase
22	lstrip()
Removes all leading whitespace in string
23	maketrans()
Returns a translation table to be used in translate function.
24	max(str)
Returns the max alphabetical character from the string str
25	min(str)
Returns the min alphabetical character from the string str
26	replace(old, new [, max])
Replaces all occurrences of old in string with new or at most max occurrences if max given
27	rfind(str, beg=0,end=len(string))
Same as find(), but search backwards in string
28	rindex( str, beg=0, end=len(string))
Same as index(), but search backwards in string
29	rjust(width,[, fillchar])
Returns a space-padded string with the original string right-justified to a total of width columns.
30	rstrip()
Removes all trailing whitespace of string
31	split(str="", num=string.count(str))
Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given
32	splitlines( num=string.count('\n'))
Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed
33	startswith(str, beg=0,end=len(string))
Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise
34	strip([chars])
Performs both lstrip() and rstrip() on string
35	swapcase()
Inverts case for all letters in string
36	title()
Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase
37	translate(table, deletechars="")
Translates string according to translation table str(256 chars), removing those in the del string
38	upper()
Converts lowercase letters in string to uppercase
39	zfill (width)
Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero)
40	isdecimal()
Returns true if a unicode string contains only decimal characters and false otherwise
