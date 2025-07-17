def op(a,b,oper):
    if oper == "+":
        return a + b
    elif oper == "-":
        return a - b
    elif oper == "*":
        return a * b
    elif oper == "/":
        return a / b
    elif oper == "%":
        return a % b
    else:
        return "Invalid operation"
print(op(10, 5, "+"))
print(op(10, 5, "-"))
print(op(10, 5, "*"))
print(op(10, 5, "/"))
print(op(10, 5, "%"))
print(op(10, 5, "^"))  # Invalid operation
    