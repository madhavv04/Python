a = 0

Products = []
    
while True:
    print("1. Jeans ")
    print("2. Shirt ")
    print("3. T-shirt ")
    print("4. Cap")
    print("0. Exit ")

    choice = input("Enter the choice you want :")

    if choice == '1' :
        
        Price = 200
        print("Price of one jeans will be 200.",end="\n\n")
        
        qty = int(input("How much quantity you want ?"))
        tot_jeans = qty * Price
        print("Amount : ",tot_jeans)
        
        Products.append("Jeans")
        print(Products)
        
        print("Do you want to buy anything else..Please select another choice :",end="\n\n")

        a = a + tot_jeans


    elif choice == '2' :
        Price = 500
        print("Price of one Shirt will be 500.",end="\n\n")
        
        qty = int(input("How much quantity you want ?"))
        tot_shirt =  qty * Price
        print("Amount : ",tot_shirt)
       
        Products.append("Shirt")
        print(Products)
        print("Do you want to buy anything else..Please select another choice :",end="\n\n")
        
        a = a + tot_shirt

    elif choice == '3':
        Price = 150
        print("Price of one T-shirt will be 150.",end="\n\n")
        qty = int(input("How much quantity you want ?"))
        tot_tshirt =  qty * Price
        print("Amount : ",tot_tshirt)

        Products.append("T-Shirt")
        print(Products)

        print("Do you want to buy anything else..Please select another choice :",end="\n\n")
        # a+=Quantity
        a = a + tot_tshirt
        
    elif choice == '4':
        Price = 250
        print("Price of one cap will be 250.",end="\n\n")
        qty = int(input("How much quantity you want ? "))
        tot_cap =  qty * Price
        print("Amount : ",tot_cap)
        Products.append("Cap")
        print(Products)
        print("Do you want to buy anything else..Please select another choice :",end="\n\n")

        a = a + tot_cap

    elif choice == '0' :
        print()
        print("Products you buy :")
        print(Products,end="\n")
        print("Your Total Amount : ")
        print(a,end='\n\n')
        break
    
    else:
        print("Invalid Choice")


print("Thank you for choosing us")
    