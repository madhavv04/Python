Teacher = []
Student = []
Question = []

while True :
    print("1. Teacher")
    print("2. Student")
    print("0. Exit")

    Decision = input("Who are you ? \n Press  : \n 1 for teacher \n 2 for Student : ")

    if Decision == "1":
       
        print("1.Register")
        print("2.Login")
        print("0.Exit")

        choice = input("IF not regitsered then register otherwise login : ")

        if choice == "1" :
            
            while True:
                email_id = input("Enter your email ID : ")
                # email_id  must contain @

                if "@" not in email_id:
                    print("@ must required")
                    email_id = input("Enter proper email_id : ")
                    continue
            
                # email_id  must contain .com 
                if ".com" not in email_id:
                    print(".com is mandatory")
                    email_id = input("Enter proper email_id : ")
                    continue

                # email_id  should not start with number
                if email_id[0].isdigit():
                    print("Email id should not start with number")
                    email_id = input("Enter proper email_id : ")
                    continue
            
                # There must be gmail yahoo hotmail 
                if not (("gmail" in email_id) or ("hotmail" in email_id) or ("yahoo" in email_id)):
                    email_id = input("Enter proper email_id : ")
                    continue
                break

            while True:
                name = input("Enter your Name : ")            
                # Name should always contains alphabets
                if not name.isalpha():
                    print("Name should contain only alphabets")
                    name = input("Enter proper name : ")
                break

            Teacher.append([email_id,name])
            print("Register Successfully")
            print(Teacher)

        if choice == "2":

            if not Teacher:
                print("First register then login")
                continue

            email_id = input("enter email id : ")
            name = input("enter name : ")

            if [email_id,name] not in Teacher:
                print("Invalid Credentials")
                continue
            print("Login Sucessfully")

            while True:

                print("1.Add Question")
                print("2.Remove Question")
                print("3.Update Question")
                print("4.Display Question")
                print("5.Delete Question")
                print("0.Exit")

                choose = input("Enter operation you want to perform : ")

                if choose == "1":
                    que = input("Enter the question you want : ")
                    opt_a = input("Enter Option A :")
                    opt_b = input("Enter Option B :")
                    opt_c = input("Enter Option C :")
                    opt_d = input("Enter Option D :")

                    while True:
                        ans = input("Enter correct answer (A/B/C/D): ")
                        if ans in ['A', 'B', 'C', 'D']:
                            Question.append({
                            "question": que,
                            "options": [opt_a, opt_b, opt_c, opt_d],
                            "answer": ans
                                })
                            print("Question added successfully!")
                            break
                        else:
                            print("Invalid! Must be A, B, C, or D")
                
                if choose == "2":
                    que = input("Enter the question you want to remove : ")


                    if que in Question:
                        for i in Question:
                            if i["question"] == que:
                                Question.remove(i)
                            print("Question remove successfully")
                    elif que not in Question:
                        print("Invalid , question not found ")
                    else:
                        print("No question available to remove")


                                  
                        
 