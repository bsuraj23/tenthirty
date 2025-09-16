def multiplication_table(num, upto=10):
    for i in range(1, upto + 1):
        print(f"{num} x {i} = {num * i}")

# Example usage
number = int(input("Enter a number: "))
multiplication_table(number)
