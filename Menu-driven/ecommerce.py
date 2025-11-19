a = 0
# i = "Yes"
while True:

    print("1. Jeans ")
    print("2. Shirt ")
    print("3. T-shirt ")
    print("4. Cap")
    print("0. Exit ")

    choice = input("Enter the choice you want :")

    if choice == 1 :
        Price = 200
        print("Price of one jeans will be 200.",end="\n\n")
        qty = int(input("How much quantity you want ?"))
        Quantity =  qty * Price
        print("Amount : ",Quantity)
        print("Do you want to buy anything else..Please select another choice :",end="\n\n")
        # a+=Quantity
        a = a + Quantity
        print("value of qty :",Quantity)
        print("value of a :",a)

    elif choice == 2 :
        Price = 500
        print("Price of one Shirt will be 500.",end="\n\n")
        qty = int(input("How much quantity you want ?"))
        Quantity =  qty * Price
        print("Amount : ",Quantity)
        print("Do you want to buy anything else..Please select another choice :",end="\n\n")
        # a+=Quantity
        a = a + Quantity
        print("value of qty :",Quantity)
        print("value of a :",a)

    elif choice == 3 :
        Price = 150
        print("Price of one T-shirt will be 150.",end="\n\n")
        qty = int(input("How much quantity you want ?"))
        Quantity =  qty * Price
        print("Amount : ",Quantity)
        print("Do you want to buy anything else..Please select another choice :",end="\n\n")
        # a+=Quantity
        a = a + Quantity
        print("value of qty :",Quantity)
        print("value of a :",a)

    elif choice == 4 :
        Price = 250
        print("Price of one cap will be 250.",end="\n\n")
        qty = int(input("How much quantity you want ? "))
        Quantity =  qty * Price
        print("Amount : ",Quantity)
        print("Do you want to buy anything else..Please select another choice :",end="\n\n")
        # a+=Quantity
        a = a + Quantity
        print("value of qty :",Quantity)
        print("value of a :",a)


    elif choice == 0 :
        print("Your Total Amount : ")
        print(a)
        break
    
    else:
        print("Invalid Choice")


        # i = input("Do you want to continue shopping ? (Yes/No): ")

print("Thank you for choosing us")
    