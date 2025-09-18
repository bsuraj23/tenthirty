#Decorators & Context Managers
#36.Execution time decorator
import time
def timing(func):
    def wrapper(*a,**kw):
        start=time
        res=func(*a,**kw)
        print('Time:',time.time()-start)
        return res
    return wrapper
#37.Count calls decorator
def count_calls(func):
    func.count=0
    def wrapper(*a,**kw):
        func.count+=1
    return func(*a,**kw)
    return wrapper
#38.Admin only decorator
def admin_only(func):
    def wrapper(user,*a,**kw):
        if user!='admin': return 'Not allowed'
        return func(user,*a,**kw)
    return wrapper
#39.File context manager
from contextlib import contextmanager
@contextmanager
def open_file(name,mode):
    f=open(name,mode)
    try: 
        yield f
    finally: 
        f.close()
#40.Change working directory
import os
@contextmanager
def change_dir(path):
    old=os.getcwd()
    os.chdir(path)
    try: 
        yield
    finally: 
        os.chdir(old)