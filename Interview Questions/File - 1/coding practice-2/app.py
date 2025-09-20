import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple argparse example")

    # Add arguments
    parser.add_argument("name", help="Your name")  # positional argument
    parser.add_argument("age", type=int, help="Your age")  # positional argument
    parser.add_argument(
        "-c", "--city", default="Unknown", help="City you live in (optional)"
    )  # optional argument

    # Parse arguments
    args = parser.parse_args()

    # Use arguments
    print(f"Hello {args.name}! You are {args.age} years old and live in {args.city}.")

if __name__ == "__main__":
    main()