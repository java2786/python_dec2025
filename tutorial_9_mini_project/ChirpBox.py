choice = None
name = None 
email = None 
password = None 


def signup():
    global name 
    global email
    global password 

    print("singup...")
    user_name = input("Enter your name: ")
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")
    
    if(len(user_name.strip())==0 or 
    len(user_email.strip())==0 or 
    len(user_password.strip())==0):
        print("Invalid details. Try again.")
    else:
        name = user_name
        email = user_email
        password = user_password
        print("Registration done")
    
    
def signin():
    print("singin...")
    print("Name:",name)
    print("Email:",email)
    print("Password:",password)
    

    
    


while choice !="3":
    print("========== Welcome to ChirpBox ==========")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if(choice == "1"):
        print("Register selected")
        signup()
    elif(choice == "2"):
        print("Login selected")
        signin()
    elif(choice == "3"):
        print("Exit")
    else:
        print("Try again")

