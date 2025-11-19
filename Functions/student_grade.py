def getStudent():

        Name = input("Enter the name of the student : ")
        
        # Total marks 
        tot_marks = int(input("Enter total number of marks : "))
        Maths = int(input("Enter the Maths marks of the student : "))
        Science = int(input("Enter the Science marks of the student : "))
        Computer = int(input("Enter the Computer marks of the student : "))
        
        #Passing of marks to calStudent function
        calStudent(Maths,Science,Computer,tot_marks)
    

def calStudent(x,y,z,tot_marks):

    # Summation of all marks obtained
    marks_obtained = x + y + z
    Percentage = (marks_obtained / tot_marks)*100

    # Passing of two varaibles to grade functions
    grade(Percentage,marks_obtained)
    

def grade(Percentage,marks_obtained):
    
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

getStudent()