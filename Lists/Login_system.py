user_data = [["user1@gmail.com","pass@123"],["user2@gmail.com","pass@456"],["user3@gmail.com","pass@789"],["user4@gmail.com","pass@101112"]]
while True :
    print("Choices : ")
    print("1.Login")
    print("2.Register")

    choice = input("Enter 1 for Login if you have account otherwise Register it first : ")

    if choice == '1' :
    
        email =  input("Enter your email : ")
        password = input("Enter your password : ")

        if [email,password] in user_data:
            print("Login successfully")
        else :
            print("Invalid email id or password ")

    elif choice == '2' :

        email =  input("Enter your email : ")
        password = input("Enter your password : ")
  
        user_data.append([email,password])
        print("Register Successfully")
    
        print(user_data)

    else :
        print("Invalid choice")

