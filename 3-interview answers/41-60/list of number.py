def write_numbers(filename, numbers):
    with open(filename, "w") as file:
        for num in numbers:
            file.write(f"{num}\n")

# Example usage
numbers = [10, 20, 30, 40, 50]
write_numbers("numbers.txt", numbers)
print("Numbers written to file.")
