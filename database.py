# subjects "database" (list of subjects)
subjects = ["Math", "English"]

#GET
def get_subjects():
    return subjects
print(get_subjects())

# POST
def add_subject(new_subject):
    subjects.append(new_subject)
    return f"{new_subject} added!"
print(add_subject("biology , chemistry , physics"))

# PUT
def update_subject(index, new_name):
    if 0 <= index < len(subjects):
        subjects[index] = new_name
        return f"Subject updated to {new_name}"
    return "Invalid index!"
print(update_subject(1, "english"))

# DELETE
def delete_subject(name):
    if name in subjects:
        subjects.remove (name)
        return f"{name} deleted!"
    return f"{name} not found!"
print(delete_subject("math , physics , economics"))