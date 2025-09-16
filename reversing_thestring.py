#reversing the string without using slicing fxn
text = "kausar fatima"
rev = ""
for char in text:
    rev = char + rev
    print(rev) #reverse my name
    
#using reverse fxn
text = "iam not good at python"
rev = "".join(reversed(text))
print(rev) #reverse the sentence