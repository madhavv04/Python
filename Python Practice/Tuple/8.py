# Print the details of all students one by one using a loop. 

student1 = (1,"ALice","Computer")
student2 = (2,"Bob","Mechanical") 
student3 = (3,"John","Civil")

all_students = (student1,student2,student3)
print(all_students)

for i in all_students:
    print(i)

for i in range(len(all_students)):
    print(all_students[i])
