def add_all(*args):
    return sum(args)
print(add_all(1,2,3,4)) 

# example 1
def show_kwargs(**kwargs):
    print("Keyword arguments received:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")
show_kwargs(name="sumanth",age=21,country="India")

#example 2
def create_profile(**kwargs):
    return kwargs
profile = create_profile(name="sumanth",course="btech", email="sumanth@gmail.com")
print(profile)

# example 3
def info(id, **kwargs):
    print("ID:", id)
    for k, v in kwargs.items():
        print(f"{k}: {v}")

info(101, name="Ali", subject="Math", marks=95)

#example 4
def total_bill(**items):
    total = sum(items.values())
    print("Items purchased:")
    for item, price in items.items():
        print(f"{item}: ₹{price}")
    print("Total bill: ₹", total)

total_bill(apple=50, milk=30, bread=25)

#example 5
def mix_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mix_args(1, 2, 3, name="Sita", age=22)

# example 6
def print_subjects(**subjects):
    for subject, marks in subjects.items():
        if marks >= 50:
            print(f"{subject}: Pass")
        else:
            print(f"{subject}: Fail")

print_subjects(Math=80, English=45, Science=60)









    











  
















    



