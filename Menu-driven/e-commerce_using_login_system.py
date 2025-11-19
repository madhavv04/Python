
User =[]

while True :
    print("------------------------")
    print("Welcome to our page : ")
    print("1.Register")
    print("2.Login")
    print("0.Exit")
    print("------------------------",end="\n\n")

    Decision = input("Press 1 for Register\nPress 2 for Login\nPress 0 for Exit \n \n --> ")

    if Decision == "1" :
        while True :
            email_id = input("Enter your email ID : ")

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
                # Also past email and name should not be same for another user
                for u in User:
                     if u[0] == email_id and u[1] == name:
                        print("User already exists with same email and name")
                        email_id = input("Enter another email_id :")
                        
                        name = input("Enter another name :")
                        # It should check for another below conditions also
                    
                        if not name.isalpha():
                            print("Name should contain only alphabets")
                            name = input("Enter proper name : ")
                
                break
        
        User.append([email_id,name,[],0])
        print(User)
        print("User Registered Successfully")
        continue

    # I want something that if there are 3 users then all users data is within them only because i want to add feature add to cart for each user

    elif Decision == "2" :
        if not User:
            print("First Register then Login")
            continue

        email_id = input("Enter your email ID : ")
        name = input("Enter your Name :")
    
    # I want to check whether the user is present or not
    # If present then only login otherwise show invalid credentials
        current_user = None
        for u in User:
             if u[0] == email_id and u[1] == name:
                  current_user = u
                  break
    
        if current_user is None:
            print("Invalid Credentials")
            continue

        print("Login Successfully")

    
    while True:
        print("----------------")
        print("|  1. Jeans    |")
        print("|  2. Shirt    |")
        print("|  3. T-shirt  |")
        print("|  4. Cap      |")
        print("|  0. Exit     |")
        print("----------------")

        choice = input("Enter the choice you want :")

        if choice == '1' :
        
            Price = 200
            print("Price of one jeans will be 200.",end="\n\n")
        
            qty = int(input("How much quantity you want ?"))
            tot_jeans = qty * Price
            print("Amount : ",tot_jeans)
        
            current_user[2].append("Jeans")
            current_user[3]+= tot_jeans
            Products = current_user[2]
            print(Products,end="\n\n")
        
            print("Do you want to buy anything else..Please select another choice :",end="\n\n")

            # a = a + tot_jeans


        elif choice == '2' :
            Price = 500
            print("Price of one Shirt will be 500.",end="\n\n")
        
            qty = int(input("How much quantity you want ?"))
            tot_shirt =  qty * Price
            print("Amount : ",tot_shirt)
       
            current_user[2].append("Shirt")
            current_user[3]+=tot_shirt
            Products = current_user[2]
            print(Products,end="\n\n")
            print("Do you want to buy anything else..Please select another choice :",end="\n\n")
        
            # a = a + tot_shirt

        elif choice == '3':
            Price = 150
            print("Price of one T-shirt will be 150.",end="\n\n")
            qty = int(input("How much quantity you want ?"))
            tot_tshirt =  qty * Price
            print("Amount : ",tot_tshirt)

            current_user[2].append("T-shirt")
            current_user[3]+=tot_tshirt
            Products = current_user[2]
            
            print(Products,end="\n\n")

            print("Do you want to buy anything else..Please select another choice :",end="\n\n")
            # a+=Quantity
            # a = a + tot_tshirt
        
        elif choice == '4':
            Price = 250
            print("Price of one cap will be 250.",end="\n\n")
            qty = int(input("How much quantity you want ? "))
            tot_cap =  qty * Price
            print("Amount : ",tot_cap)
            current_user[2].append("Cap")
            current_user[3]+=tot_cap
            Products = current_user[2]
            print(Products,end="\n\n")
            print("Do you want to buy anything else..Please select another choice :",end="\n\n")

            # a = a + tot_cap

        elif choice == '0' :
            # Current user add to cart as shown below with products and total amount
            Products = current_user[2]
            Total_Amount = current_user[3]
            #list should be converted into tuple for better understanding
            Products = tuple(Products)
            print("----------------------------------")
            print("Products you buy : ", Products)
            print("Your Total Amount : ", Total_Amount)
            print("----------------------------------")
            break
    
        else:
            print("Invalid Choice")

    print("Thank you for choosing us")

    # at last i want to show only add to cart of all users who have registered and logged and bought products
    print("All users who have registered and logged in and bought products :")
    for u in User:
         Products = tuple(u[2])
         Total_amount = u[3]
         print(f"User :{u[1]} \n Products : {Products} \n Total Amount : {Total_amount}",end="\n\n")
         
    

   
    