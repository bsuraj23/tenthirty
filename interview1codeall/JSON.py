#Serialize and deserialize with JSON
import json
data={'a':1,'b':2}
s=json.dumps(data)
print(json.loads(s))

#Read command line args with argparse.
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('Sindhu')
args=parser.parse_args()
print("Hello",args.Sindhu)