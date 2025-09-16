from mypackage import add, multiply, concat_and_sum_lengths

print("Add 5 + 7 =", add(5, 7))
print("Multiply 3 * 4 =", multiply(3, 4))
combined, length_sum = concat_and_sum_lengths("Hello", "World")
print("Combined string:", combined)
print("Sum of lengths:", length_sum)
