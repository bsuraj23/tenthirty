import re
# extraction
pattern = r"[\w\.-]+@[\w\.-]+.[\w{2,}$]"
text= "emails are soham@gmail.com and chintu@email.com"

mail= re.findall(pattern,text)
print(mail)

#validation 

pattern2= r"[\w]{3,}.+[\w.-]+@[\w.-]+.[\w{2,}$]"
text2=["www.sohamraibole@hmail.com","www.xyzABC@gmail.com"]

for m in text2:
    if re.fullmatch(pattern2,m):
        print("valid mail")
        
    else:
        print("invalid mail")
            