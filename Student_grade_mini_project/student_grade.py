Total = int(input("Enter the marks for evaluation : "))
Maths = int(input("Enter the marks for : Maths - "))
Chemistry = int(input("Enter the marks for : Chemistry - "))
Physics = int(input("Enter the marks for : Physics - "))
Computer = int(input("Enter the marks for : Computer - "))
Biology = int(input("Enter the marks for : Biology - "))

marks_obtained = Maths + Chemistry + Physics + Computer + Biology
Percentage = (marks_obtained/Total)*100 

if Percentage > 90:
    print("Grade A","Marks Obtained : ",marks_obtained,"Percentage : ",Percentage)

elif Percentage > 80 and Percentage <=90:
    print("Grade B","Marks Obtained : ",marks_obtained,"Percentage : ",Percentage)
 
elif Percentage > 70 and Percentage <=80:
    print("Grade C","Marks Obtained : ",marks_obtained,"Percentage : ",Percentage)

elif Percentage > 60 and Percentage <=70:
    print("Grade D","Marks Obtained : ",marks_obtained,"Percentage : ",Percentage)

else:
    print("Fail","Marks Obtained : ",marks_obtained,"Percentage : ",Percentage)
