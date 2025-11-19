User = []
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