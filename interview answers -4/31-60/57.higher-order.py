#57.Explain higher-order functions with real-world use cases.
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30
