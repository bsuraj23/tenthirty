x={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
x['e']=6
print(x)
student={'name':"Rizwan" ,'age':21 ,'branch':"aiml"}
updated={}
for keys, value in student.items():
    new='student_'+keys
    updated[new]=value
print(updated)
student["student_year"]="final"
print(student)