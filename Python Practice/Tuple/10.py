
# Check if a particular course (e.g., “Python”) is present in any student’s tuple by using the in keyword. 

student1 = (1,"ALice","Computer")
student2 = (2,"Bob","Mechanical") 
student3 = (3,"John","Civil")

all_students = (student1,student2,student3)
print(all_students)

check = "Python"

for student in all_students:
    if check in student:
        print(f"{check} is present in {student}")
    else:
        print(f"{check} is not present in {student}")