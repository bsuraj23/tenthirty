import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name", help="your name")
parser.add_argument("age", type=int,help="your age ")

a= parser.parse_args()
print(f"hello {a.name} of age {a.age}")