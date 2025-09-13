#writing and reading a file 

with open("myfile.txt","w") as f:
    f.write("my file is created ")

with open ("myfile.txt","r") as f:
    content = f.read()
    print(content)
    

# handling csv file

import csv
with open ("file1.csv","w", newline="") as f:
    writer= csv.writer(f)
    writer.writerow(["Name","Age"])
    writer.writerow(["soham",22])
    writer.writerow(["xyz",45])         #remember csv.writer/csv.reader
    
with open ("file1.csv","r") as f:
    reader= csv.reader(f)
    
    for rows in reader:
        print(rows) 
        
import json

#json serialization & deserializarion
# Serialize
data = {"name": "Soham", "age": 22}
json_str = json.dumps(data)       # to string
with open("data.json", "w") as f:
    json.dump(data, f)            # to file

# Deserialize
loaded_str = json.loads(json_str)  # from string
with open("data.json", "r") as f:
    loaded_file = json.load(f)     # from file

print(loaded_str)   # {'name': 'Soham', 'age': 22}
print(loaded_file)  # {'name': 'Soham', 'age': 22}
     