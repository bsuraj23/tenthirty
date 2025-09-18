#Data Handling

#Read a text file and count the number of words
def word_count(filename):
    with open(filename, "r") as f:
        text = f.read()
        words = text.split()
        return len(words)
#create a file named sample.txt
print("Word count:", word_count("sample.txt"))

#Write a function that writes a list of numbers to a file (one per line)
def write_numbers(filename, numbers):
    with open(filename, "w") as f:
        for num in numbers:
            f.write(str(num) + "\n")

write_numbers("numbers.txt", [10, 20, 30, 40, 50])

#Read a CSV file and print only the second column values
import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 1:   
            print(row[1])

#Serialize a dictionary into JSON and back
import json
data = {"name": "Alice", "age": 25, "city": "Paris"}
# Serialize (dict → JSON string)
json_string = json.dumps(data)
print("JSON string:", json_string)
# Deserialize (JSON string → dict)
dict_data = json.loads(json_string)
print("Dictionary:", dict_data)
