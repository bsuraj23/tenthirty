#Write a decorator that only allows function execution if the user is "admin".
from functools import wraps

def admin_only(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print(f"Access denied for user '{user}'. Only admin can execute this function.")
            return None
        return func(user, *args, **kwargs)
    return wrapper


# Example usage
@admin_only
def delete_all_data(user):
    print("All data has been deleted!")


# Test calls
delete_all_data("admin")   # Allowed
delete_all_data("guest")   # Denied
