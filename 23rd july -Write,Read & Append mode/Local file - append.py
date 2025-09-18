file_path = r"C:\Users\Srikanth_09\Documents\Write mode.txt"
text_to_add = "This line is added using append mode in Python.\n"

with open(file_path, 'a') as file:
    file.write(text_to_add)
