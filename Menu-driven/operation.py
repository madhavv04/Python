
i = "Yes"

while i == "yes":   
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter the operation you want to perform : "))

    if choice == 1:
        a = int(input("Enter the value for a :")) 
        b = int(input("Enter the value for b :"))
        print("Sum =", a + b)

    elif choice == 2:
        a = int(input("Enter the value for a :")) 
        b = int(input("Enter the value for b :"))
        print("Subtraction =", a - b)

    elif choice == 3:
        a = int(input("Enter the value for a :")) 
        b = int(input("Enter the value for b :"))
        print("Multiplication =", a * b)

    elif choice == 4:
        a = int(input("Enter the value for a :")) 
        b = int(input("Enter the value for b :"))
        if b != 0:
            print("Division =", a / b)
        else:
            print("Error: Division by zero not allowed.")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

    
    i = input("Do you want to continue? (Yes/No): ")

print("Thank you")
