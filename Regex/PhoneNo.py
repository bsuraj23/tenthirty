#extraction of number 
import re
pattern = r"[0-9]\d{9}"
text= "Phone numbers are 7620268573  and 9401865724"

phones = re.findall(pattern,text)
print(phones)

#validation
pattern2 = r"[0-9]\d{9}"
text2 = ["8745739754","7945634975"]
for t in text2:
    if re.fullmatch(pattern2,t):
        print("valid number")
    else:
        print ("invalid number")            