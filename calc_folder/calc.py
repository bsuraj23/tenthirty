##55Implement a script that accepts command-line arguments for addition and subtraction.
import sys

def main():
    if len(sys.argv) < 4:
        print("Usage: python calc.py <add|sub> num1 num2")
        return

    operation = sys.argv[1].lower()
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])

    if operation == "add":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "sub":
        print(f"{num1} - {num2} = {num1 - num2}")
    else:
        print("Unknown operation. Use 'add' or 'sub'.")

if __name__ == "__main__":
    main()
