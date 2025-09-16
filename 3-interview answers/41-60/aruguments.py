import argparse

def main():
    parser = argparse.ArgumentParser(description="Perform addition or subtraction")
    parser.add_argument("a", type=int, help="First number")
    parser.add_argument("b", type=int, help="Second number")
    parser.add_argument("--operation", choices=["add", "sub"], default="add", help="Operation to perform")
    
    args = parser.parse_args()

    if args.operation == "add":
        result = args.a + args.b
    else:
        result = args.a - args.b

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
