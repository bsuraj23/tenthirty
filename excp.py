# Define a custom exception
class InvalidAgeError(Exception):
    pass

def validate_age(age):
    try:
        if age < 0:
            raise InvalidAgeError("Age cannot be negative!")
        elif age < 18:
            print("❗ You must be at least 18.")
        else:
            print("✅ Access granted.")
    except InvalidAgeError as e:
        print(f"🚫 Error: {e}")
    except Exception as e:
        print(f"🔍 Unexpected error: {e}")
    finally:
        print("🔚 Validation complete.\n")


