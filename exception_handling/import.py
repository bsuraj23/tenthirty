import sys
sys.path.append(r"C:\Users\chman\OneDrive\Desktop\Python\Function")

try:
    import fun1
except ImportError:
    print("Module not found")
