#Json handling files

#converting python to json
import json
python_dict={
  "name": "Harish",
  "age": 21,
  "skills": ["Python", "FastAPI"]
}
print("Converting python to json")
json_string=json.dumps(python_dict)    #Function: dumps or dump
print(type(python_dict),json_string,type(json_string),)   #if it is a string it is a json data, if it is a dict it is a python data

with open("python_dict.json","w") as f:
    json.dump(python_dict, f)

#converting json to python
print("Converting JSON to pyhton")
json_strings='{"name": "Harish", "age": 23, "skills": ["Python", "FastAPI"]}'
python_dict=json.loads(json_strings)
print(type(json_strings),python_dict,type(python_dict))

with open("python_dict.json","r") as f:
    data=json.load(f)
print(data)

