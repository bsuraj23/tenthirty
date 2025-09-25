#multiple exceptions in one exception
try:
    x=int("abc")
    y=11/0
except (ValueError, ZeroDivisionError) as e:
    print("Handled:",e)