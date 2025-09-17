#custom contextlib 
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering the context")
    yield "Resource ready"   #yield can stop here 
    print("Exiting.....")    #but with is the statement used for safe resource management

with my_context() as res:
    print(res)
