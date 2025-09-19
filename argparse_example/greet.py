#Implement a small script that reads command line arguments with `argparse`.
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple greeting program.")

# Add arguments
parser.add_argument('name', type=str, help="Your name")
parser.add_argument('--age', type=int, help="Your age", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.age:
    print(f"Hello, {args.archana}! You are {args.age} years old.")
else:
    print(f"Hello, {args.archana}!")


