class validator:
    @staticmethod
    def is_even(num):
        return num%2==0

print(validator.is_even(10))
print(validator.is_even(7))