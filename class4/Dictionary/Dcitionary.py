d = {'a': 1, 'b': 2}
d2 = dict(name='John', age=30)
d3 = {'x': 100, 'y': 200}
d4 = dict([('a', 1), ('b', 2)])
d5 = {1: 'one', 2: 'two'}
print(d.keys())
print(d.values())
print(d.items)
print("d2.keys:", d2.keys())
print("d3.values:", d2.values())
print("d4.keys:", d3.keys())
print("d4.values:", d4.values())
print("d5.keys:", d5.keys())
print("d5.values:", d5.values())


#dictionary in list output
d={'a':1, 'b':2}
d2=dict(name='archana', age='21')
d3={'x':100,'y':200}
d4=dict([('a', 1),('b', 2)])
d5={1:'one', 2:'two'}
dicts=[d,d2,d3,d4,d5]
for i, dict in enumerate(dicts,start=1):
    print(f"\nDictionary d{i}:")
    print("keys:", list(dict.keys()))
    print("values",list(dict.values()))
    print("items", list(dict.items()))
    #
student={"name":'archu', "age":'20'}
print(student["name"])
print(student["age"])
#
student={"name":'archu', "age":'20'}
student["course"]="python"
student["age"]=21
print(student)
#
student={"name":'archu', "age":'20', "course":'python'}
student.pop("age")
print(student)
#
student={"name":'archu', "age":'20'}
print(student.keys())
print(student.values())