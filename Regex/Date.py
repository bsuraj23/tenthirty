import re
pattern= r"\d{2}/\d{2}/\d{4}"  #extarction
text="my birth date is 30/04/2003"
date= re.findall(pattern, text)
print(date)

#  validation

pattern2 =r"\d{2}/[\w.-]{3}/\d{4}"
text=["30apr2003","12dec2012"]

for d in text:
    if re.fullmatch(pattern2,d):
        print("valid date")
    else:
        print("invalid date")    