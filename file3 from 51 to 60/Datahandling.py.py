#Count words in a file
#51.count_words.py
def count_words_stream(path):
    count = 0
    with open(path,'r',encoding='utf-8') as f:
        for line in f:
            count += len(line.split())
    return count
#52.Write a list to a file
#write_numbers.py
def write_numbers(lst, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for n in lst:
            f.write(str(n) + '\n')

if __name__ == '__main__':
    nums = [10, 20, 30]
    write_numbers(nums, 'out.txt')
    print("Wrote", len(nums), "lines to out.txt")
#53.Print the CSV second column
# print_second_col.py
import csv

with open('file.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 1:
            print(row[1])
        else:
            print('(no 2nd column)')
#54.JSON serialize & deserialize
# json_example.py
import json

data = {'a': 1, 'b': [1, 2, 3]}
js = json.dumps(data)       
print("JSON string:", js)

back = json.loads(js)       
print("Parsed back:", back)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

with open('data.json', 'r', encoding='utf-8') as f:
    loaded = json.load(f)
    print("Loaded from file:", loaded)
#55.Add two command-line arguments
#add.py
import sys

if len(sys.argv) < 3:
    print("Usage: python add.py NUM1 NUM2")
    sys.exit(1)

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except ValueError:
    print("Please supply two integers.")
    sys.exit(1)

print('Sum:', a + b)