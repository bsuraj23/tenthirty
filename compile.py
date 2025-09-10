# Define Python source code as a string
source_code = """
def square(n):
    return n * n

result = square(9)
print("Square of 9 is:" , result)
"""

# Compile the code string into a code object
code_object = compile(source_code, filename="<string>", mode="exec")

# Execute the compiled code
exec(code_object)
