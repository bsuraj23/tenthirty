d={'a':1,'b':2,'c':3,'d':4}
d['b']=5
print(d)
student={"name":"Harish","age":21,"course":"cse"}
updated={}
for key, value in student.items():
    new= "student_" +key
    updated[new]=value
print(updated)
student["student_year"]="Final"
print(student)