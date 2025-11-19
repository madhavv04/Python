user_data = [
       { "email" : "abc@gmail.com" ,"password": "pass@123"},
       { "email" : "def@gmail.com" ,"password": "pass@456"},
       { "email" : "ghi@gmail.com" ,"password": "pass@789"},
       { "email" : "xyz@gmail.com" ,"password": "pass@101112"},
       { "email" : "pqr@gmail.com" ,"password": "pass@121314"},
    
]
while True:
    print("1.Login")
    print("2.Register")

    choice = input("Enter your choice : 1 for Login and 2 for Register if you do not have account : ")

    if choice == '1':

        email = input("Enter your email address : ")
        password = input("Enter your password : ")

        if {"email":email,"password":password} in user_data:
            print("Login Successfully")
        else :
            print("Invalid username or password")

    if choice == '2':

        email = input("Enter your email address : ")
        password = input("Enter your password : ")
        user_data.append({"email":email,"password":password})
        print(user_data)



     







# elif choose == "2":
#                 ques = input("Enter question you want to remove : ")
#                 for i in Question:
#                     if i["Question"] == ques:
#                         Question.remove(i)
#                         print("Question removed successfully")
#                         print(Question)
#                 else:
#                     print("Question not found")
                    
#             elif choose == "3":
#                 ques = input("Enter question you want to update : ")
#                 for i in Question:
#                     if i["Question"] == ques:
#                         print("Current Question : ", i["Question"])
#                         print("Current Options : ", i["Options"])
#                         print("Current Answer : ", i["Answer"])
#                         new_ques = input("Enter new question : ")
#                         new_opt = input("Enter new options : ")
#                         new_ans = input("Enter new answer : ")
#                         i["Question"] = new_ques
#                         i["Options"] = new_opt
#                         i["Answer"] = new_ans
#                         print("Question updated successfully")
#                         print(Question)
#                 else:
#                     print("Question not found")

#             elif choose == "4":
#                 if Question:
#                     for i in Question:
#                         print("Question : ", i["Question"])
#                         print("Options : ", i["Options"])
#                         print("Answer : ", i["Answer"])
#                         print()
#                 else:
#                     print("No questions available")
        
#             elif choose == "5":
#                 Question.clear()
#                 print("All questions deleted successfully")
#                 print(Question)
                
#             elif choose == "0":
#                 break

#             else:
#                 print("Invalid choice")
