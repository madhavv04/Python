from register_function import User

def login():
    
        email_id = input("Enter your email ID : ")
        name = input("Enter your Name : ")

        

            
        current_user = {}
        for u in User:
            print(u)
            if u["email"] == email_id and u["name"] == name:
                current_user = u
                break

        if current_user is None:
            print("Invalid Credentials")
            return None

        print(f" Welcome , {current_user['name']}!")
        return current_user


