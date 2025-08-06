import multiprocessing
def task():
    print("This is a separate process!")

if __name__=="__main__":
    #creating a process
    process = multiprocessing.Process(target=task)
    print("Process created:", process)
