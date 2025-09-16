import csv

def print_second_column(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                print(row[1])

# Example usage
print_second_column("data.csv")
