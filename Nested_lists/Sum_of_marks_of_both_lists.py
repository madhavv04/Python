# Marks of two students
std_data = [[10,20,30,40,50],[60,70,80,90,100]]
total_marks=[0,0,0,0,0]

for i in range(len(std_data[0])):
    total_marks[i] = std_data[0][i]+std_data[1][i]
    print(total_marks)