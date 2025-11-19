Teacher = []
Question = []
Student = []

while True:
    print("-"*50)
    print("1. Teacher")
    print("2. Student")
    print("0. Exit")
    print("-"*50)


    Decision = input("Who are you ? \n Press  : \n 1 for teacher \n 2 for Student : ")

    if Decision == "1" :
    
        print("1.Register")
        print("2.Login")
        print("0.Exit")

        choice = input("Enter your choice : ")

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
        
        elif choice == "2":
            # if user is registered then only login accessed allowed
            if not Teacher:
                print("NO teacher registered yet. Please register first.")
                continue 

            # Also takes email and name for login to that teacher account only and changes will be done in that account only
            email_id = input("Enter your email ID : ")
            name = input("Enter your Name :")
            
            if [email_id, name] not in Teacher:
                print("Invalid credentials. Please register first.")
                continue
            # If credentials are correct then only login success
            print("Login successfully")


            while True :
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

                elif choose == "2":
                    ques = input("Enter question you want to remove : ")
                    found = False
                    for i in Question:
                        if i["question"] == ques:
                            Question.remove(i)
                            print("Question Removed Successfully")
                            print(Question)
                            found = True
                            break
                        if not found :
                            print("Question not found")
            
                elif choose == "3":
               
                    ques = input("Enter the question you want to update : ")
                    for i in Question:
                        if i["question"] == ques:
                            new_que = input("Enter new question : ")
                            opt_a = input("Enter new Option A : ")
                            opt_b = input("Enter new Option B : ")
                            opt_c = input("Enter new Option C : ")
                            opt_d = input("Enter new Option D : ")
                            
                            while True:
                                ans = input("Enter correct answer (A/B/C/D): ")
                                if ans in ['A', 'B', 'C', 'D']:
                                    break
                                else :
                                    print("Invalid! Must be A, B, C, or D")

                        i["question"] = new_que
                        i["options"] = [opt_a,opt_b,opt_c,opt_d]
                        i["answer"] = ans

                        print("Question updated successfully")
                        break
                    
                    else :
                        print("Question not found")

                elif choose == "4":
                    print("All Questions : ")
               
                    for i in Question:
                        print(i["question"])
                        print(" A:", i["options"][0])
                        print(" B:", i["options"][1])
                        print(" C:", i["options"][2])
                        print(" D:", i["options"][3])
                        print(" Correct Answer:", i["answer"])

                elif choose == "5":
                    Question.clear()
                    print("All Questions deleted")
            
            #Teacher Login choose exit point
                elif choose == "0":
                    break

                else:
                    print("Invalid choice")
    
    elif Decision == "2":

        print("1.Register")
        print("2.Login")

        choice = input("Enter your choice : ")

        if choice == "1":
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
             
                Student.append([email_id,name])
                print("Register Successfully")
                print(Student)
                break

        elif choice == "2":
            
            if not Student:
                print("No student registered yet. Please register first.")
                continue
            
            email_id = input("Enter your email ID : ")
            name = input("Enter your Name :")
           
            if [email_id, name] not in Student:
                print("Invalid credentials. Please register first.")
                continue
            print("Login successfully")
            
            print("Exam Started!")
            score = 0
            for i in Question:
                print("\nQ:", i["question"])
                print("A:", i["options"][0])
                print("B:", i["options"][1])
                print("C:", i["options"][2])
                print("D:", i["options"][3])

                ans = input("Enter answer (A/B/C/D): ")
                while ans not in ['A', 'B', 'C', 'D']:
                    ans = input("Invalid! Enter again (A/B/C/D): ")

                if ans == i["answer"]:
                    score += 1
                    print("Correct!")
                else:
                    print("Wrong! Correct answer is:", i["answer"])

            print("\n Final Score:", score, "/", len(Question))
            
        elif choice == "0":
            break
        
        else:
            print("Invalid choice")

    # Decision Exit point
    elif Decision == "0":
        break

    else:
        print("Invalid Choice")


 
            