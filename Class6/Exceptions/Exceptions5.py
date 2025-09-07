try:
    # open("C:\Users\Suraj\Desktop\GreenWorkSpace1\A2JulyWorkSpace\PythonAllCodes-main\Class6")
     open("nonexistent.txt")
except FileNotFoundError:
    print("File does not exist Pleaase check the existence of file ")
