#we cannot directly add a string and an integer (like "5" + 3) 
#_ this will raise a TypeError.So, you need to convert 
#one type to another before adding.
def add_string_and_integer(s: str, n: int) -> int:
    # Convert string to integer
    converted = int(s)
    result = converted + n
    return result

# Example usage
string_input = "5"
integer_input = 3

output = add_string_and_integer(string_input, integer_input)
print("Result:", output)
