User = []

def register():
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
    
    f=open(name,'x')
    f=open(name,'w')
    f.write(f'Name:{name}\nEmail ID:{email_id}\n')
    f.close()
    
