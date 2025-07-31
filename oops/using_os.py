import os

#current directory
print(os.getcwd())

#list files in current directory
print(os.listdir())
# Example: Create a new directory
#os.mkdir('txt_files')
file= open('class_cr.py', 'w')
#remove a file
os.remove('class_cr.py')  # Uncomment to remove a file