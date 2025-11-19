
User = []

while True:
    print("------------------------")
    print("Welcome to our page : ")
    print("1.Register")
    print("2.Login")
    print("0.Exit")
    print("------------------------", end="\n\n")

    Decision = input("Press 1 for Register\nPress 2 for Login\nPress 0 for Exit \n\n--> ")

    # ---------------- REGISTER ----------------
    if Decision == "1":
        while True:
            email_id = input("Enter your email ID : ")

           
            if "@" not in email_id:
                print("@ must required")
                continue
           
            if ".com" not in email_id:
                print(".com is mandatory")
                continue
           
            if email_id[0].isdigit():
                print("Email id should not start with number")
                continue
           
            if not (("gmail" in email_id) or ("hotmail" in email_id) or ("yahoo" in email_id)):
                print("Email must be gmail, hotmail or yahoo")
                continue
           
            # Check duplicate email
            if any(u["email"] == email_id for u in User):
                print("This email is already registered.")
                continue
            break

        while True:
            name = input("Enter your Name : ")
            if not name.isalpha():
                print("Name should contain only alphabets")
                continue
            break

        User.append({
            "email": email_id,
            "name": name,
            "cart": [],
            "total": 0
        })
        print("User Registered Successfully!\n")
        continue

    # ---------------- LOGIN ----------------
    elif Decision == "2":
        if not User:
            print("First Register then Login")
            

        while True:
            email_id = input("Enter your email ID : ")

           
            if "@" not in email_id:
                print("@ must required")
                continue
           
            if ".com" not in email_id:
                print(".com is mandatory")
                continue
           
            if email_id[0].isdigit():
                print("Email id should not start with number")
                continue
           
            if not (("gmail" in email_id) or ("hotmail" in email_id) or ("yahoo" in email_id)):
                print("Email must be gmail, hotmail or yahoo")
                continue
           
            # Check duplicate email
            if any(u["email"] == email_id for u in User):
                print("This email is already registered.")
                continue
            break

        while True:
            name = input("Enter your Name : ")
            if not name.isalpha():
                print("Name should contain only alphabets")
                continue # continue is used to skip the current iteration and move to the next iteration of the loop.
            break

        User.append({
            "email": email_id,
            "name": name,
            "cart": [],
            "total": 0
        })
        print("User Registered Successfully!\n")
        
        current_user = None
        for u in User:
            if u["email"] == email_id and u["name"] == name:
                current_user = u
                break

        if current_user is None:
            print("Invalid Credentials")
            continue

        print(f" Welcome , {current_user['name']}!")

        # ---------------- SHOPPING MENU ----------------
        while True:
            print("----------------")
            print("|  1. Jeans    |  ₹200 each")
            print("|  2. Shirt    |  ₹500 each")
            print("|  3. T-shirt  |  ₹150 each")
            print("|  4. Cap      |  ₹250 each")
            print("|  0. Checkout |")
            print("----------------")

            choice = input("Enter the choice you want : ")

            if choice == '1':
                product = "Jeans"
                price = 200
            elif choice == '2':
                product = "Shirt"
                price = 500
            elif choice == '3':
                product = "T-shirt"
                price = 150
            elif choice == '4':
                product = "Cap"
                price = 250
            elif choice == '0':
                # ---------------- CHECKOUT ----------------
                print("\n----------------------------------")
                print(f" Bill for {current_user['name']} ({current_user['email']})")
                print("----------------------------------")

                if not current_user["cart"]:
                    print("Your cart is empty.")
                else:
                    total_amount = 0
                    print(f"{'Product':<12}{'Qty':<8}{'Price':<10}{'Amount'}")
                    print("-" * 40)
                    for item in current_user["cart"]:
                        pname = item["product"]
                        qty = item["quantity"]
                        price = item["price"]
                        amount = qty * price
                        total_amount += amount
                        print(f"{pname:<12}{qty:<8}{price:<10}{amount}")

                    print("-" * 40)
                    print(f"{'Total Amount':<30}₹{total_amount}")
                    print("----------------------------------")

                    # Empty the user’s cart after checkout
                    current_user["cart"].clear()
                    current_user["total"] = 0

                print("Thank you for shopping with us!\n")
                break

            else:
                print("Invalid choice, try again.\n")
                continue

            qty = int(input(f"How many {product}s you want? : "))
            total = qty * price
            print(f"Amount for {qty} {product}(s): ₹{total}\n")

            current_user["cart"].append({
                "product": product,
                "quantity": qty,
                "price": price
            })
            current_user["total"] += total

            print("Added to cart successfully!\n")

    # ---------------- EXIT ----------------
    elif Decision == "0":
        print("\nAll users who registered and bought products:\n")
        for u in User:
            print(f"User : {u['name']}  ({u['email']})")

            if u["cart"]:
                print(f"{'Product':<12}{'Qty':<8}{'Price':<10}{'Amount'}")
                print("-" * 40)
                total = 0
                for item in u["cart"]:
                    pname = item["product"]
                    qty = item["quantity"]
                    price = item["price"]
                    amount = qty * price
                    total += amount
                    print(f"{pname:<12}{qty:<8}{price:<10}{amount}")
                print("-" * 40)
                print(f"Total Amount : ₹{total}")
            else:
                print("No products purchased.")
            print("----------------------------------\n")

        print("Thank you for visiting!")
        break

    else:
        print("Invalid Input. Please try again.")
    