import argparse

# Create parser
parser = argparse.ArgumentParser(description="Demo of argparse")

# Add arguments
parser.add_argument("--name", type=str, help="swathi")
parser.add_argument("--age", type=int, help="21")

# Parse arguments
args = parser.parse_args()

# Use arguments
print(f"Hello {args.pooja}, you are {21} years old!")
