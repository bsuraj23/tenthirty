class Mycontext:
    def __enter__(self):
        print("Entering the context...")
        return 'Resource ready'
    def __exit__(self, exe_type,exe_value,traceback):
        print("Exiting the context....")
        if exe_type:
            print(f"An error occured: {exe_value}")
        return True

with Mycontext() as resource:
    print(resource)
    