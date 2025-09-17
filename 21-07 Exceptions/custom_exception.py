class MyCustomError(Exception):
    """This is a custom Exception"""
    pass

try:
    raise MyCustomError("Something went wrong in my program!")
except MyCustomError as e:
    print("Caught custom Exception:", e)
