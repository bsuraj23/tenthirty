import re
#extraction 
pattern = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
text= "my pan card number is EXHPR3555P and my fathers is ASDFG1234G"

pan= re.findall(pattern,text)
print(pan)

#validation
pattern2 = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
text2=["YETIY5423Y","hf64fybjf"]

for p in text2:
    if re.fullmatch(pattern2,p):
        print("valid pan number")
    else :
        print("invalid pan  number")    