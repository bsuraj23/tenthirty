# Global scope
x = "global_x"

def outer():
    # Enclosing (nonlocal) scope
    x = "enclosing_x"

    def inner():
        # Local scope
        x = "local_x"
        print("Inside inner():", x)  # Accesses local x

    inner()
    print("Inside outer():", x)      # Accesses enclosing x

outer()
print("In global scope:", x)          # Accesses global x
