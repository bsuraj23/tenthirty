try:
    import non_existing_module
except ModuleNotFoundError:
    print("Module not found")
