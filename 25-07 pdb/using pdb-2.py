import pdb
def calculate_total(marks):
    total=0
    for mark in marks:
        pdb.set_trace()
        total = total+mark
    return total
student_marks = [75,65,89,60,74,90]
result=calculate_total(student_marks)
print("Total marks:",result)