import re
#extraction
pattern= r"\d{12}"
text= " my aadhar no is 123456789101"

adhar= re.findall(pattern, text)
print(adhar)

#validation
adharno=['123456789012','98768']

for a in adharno:
    if re.fullmatch(pattern,a):
        print("valid adhar number")
    else :
        print("invalid adhar number ")    
