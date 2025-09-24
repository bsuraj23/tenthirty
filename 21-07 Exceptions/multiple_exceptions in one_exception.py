#multiple exceptions in one exception
try:
    x=int("abc")
    y=10/0
except (ValueError, ZeroDivisionError) as e:
    print("Handled:",e)