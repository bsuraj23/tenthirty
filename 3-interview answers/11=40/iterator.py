# Create a custom iterator class that generates square numbers up to `n`.
class SquareIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            square = self.current ** 2
            self.current += 1
            return square
        else:
            raise StopIteration


# Example usage
squares = SquareIterator(5)
for num in squares:
    print(num)
