#example 1
days = ["Monday", "Tuesday", "Saturday", "Wednesday", "Sunday", "Thursday"]

for day in days:
    if day in ["Saturday", "Sunday"]:
        continue  
    print(f"{day}: Working day")



#example 2
for i in range(10):
    if i == 4:
        continue
    print(i)
