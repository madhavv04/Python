while True:
    
    a = [] # a is empty list

    elements = int(input("Enter elements of list: ")) # Enter the element you want to insert 
    
    # Choices of this program

    print("1.Add a single element") 
    print("2.Exit")
    
    choice = int(input("Enter your choice: "))
    
    # If choice is 2 then it will break and end the program
    if choice == 2:
        break
    
    # If choice is 1 then it will continue executing the program until while loop is True
    elif choice == 1:
        a.append(elements)
        print(a)