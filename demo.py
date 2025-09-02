f = open("demo.txt", "a+")  # Append and read mode
f.write("sumanth")            # Append data
f.seek(0)                   # Move to beginning
print(f.read())             # Read full file
f.close()
