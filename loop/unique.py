n=[1,2,2,3,4,5,5,6,"m","ma","m","m",1,2,3,4,5,6]
unique_list = []
# Loop through each element in the list

for i in n:
    # Check if the element is not already in the unique list
    if i not in unique_list:
        # If not, append it to the unique list
        unique_list.append(i)

# Print the unique elements
print("Unique elements:", unique_list)