#Implement a class with a **static method** to check if a number is even.
class NumberUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0


# Example usage
print(NumberUtils.is_even(10))  # True
print(NumberUtils.is_even(7))   # False
