#without with statement 
f=open("test.txt",'w')
f.write("Hello Harish")
f.close()

#with statement (context manager)

with open("pen.txt",'w') as f:
    f.write("welcome to pen file")  #in this with statement file the file pen which you created now that will
    #automatically closed, here no need to use f.close() because when you use with statement that will close automatically
    #this method with statement is called context manager
    