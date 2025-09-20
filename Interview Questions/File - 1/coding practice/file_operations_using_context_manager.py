#Write a **context manager** to handle file operations.

class FileManager:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    def __enter__(self):
        print(f"Opening file:{self.filename}")
        self.file=open(self.filename,self.mode,encoding='utf-8')
        return self.file
    def __exit__(self, exe_type, exe_value, traceback):
        if self.file:
            self.file.close()
            print(f"Closing file:{self.filename}")
        if exe_type:
            print(f"Error Occured:{exe_value}")
        return False

if __name__=="__main__":
    with FileManager("example.txt","w") as f:
        f.write("Hello, Iam Harih Reddy, did you recognised me, i used context manager!")

    with FileManager("example.txt","r") as f:
        print("File content:", f.read())
