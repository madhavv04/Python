# Marks of two students
std_data = [[10,20,30,40,50],[60,70,80,90,100]]

for i in std_data: # iterating through each list
    total_marks = 0 # must be reset
    for j in i:
        total_marks += j
    print(total_marks)