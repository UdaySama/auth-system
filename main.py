
# menu = True
registered = False
# home =  True
logged_in = False

def get_input(message,error_Msg):
    value = input(message)
    value=value.strip()
    while not value:
        print(error_Msg)
        value = input(message)
        value=value.strip()
    return value

def get_Int(message, error_Msg): 
    while True:
        user_input = input(message)
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print(error_Msg)
            # print("Invalid Input")  
    return user_input

def option_choose(choices,message,error_Msg):
    while True:
        choice = get_Int(message, error_Msg)
        if choice in choices:
            break   # keeping/added it beacuse to i think condition will fullfill then loop will end 
        else:
            print(error_Msg)
    return choice 


def show_menu():
    if logged_in:
        print("""
                1. Home
                2. Chnage Password
                3. Logout
            """)
    else:
        print("""
                1. Register
                2. Login
                3. Exit
            """)

while True:
    print("========== AUTH APP ==========")
    show_menu()

    print("==============================")

    # try:
    # choice=int(input("Enter choice:- "))
    # choice = get_Int("Enter choice:- ","Please enter a number")  # this is right ok
    choice = option_choose([1,2,3],"Enter choice:- ","Please enter a valid choice")  # this is right ok

    if choice == 1:
        if registered:
            print("user already registered")
        else:
            username = get_input("Entre Username:- ","Please enter a username")
            password = get_input("Entre Password:- ","Please enter a Password")
            user = {
             "username" :username,
             "password":password
            }
            registered = True
            print("Welcome, ",username)
            print("Registration Successful!")
    elif choice == 2:
        if registered:
            username = get_input("Entre Username:- ","Please enter a username")
            password = get_input("Entre Password:- ","Please enter a Password")
            
            if username == user["username"] and password == user["password"]:
                print(f"""
                    Login successful!
                    Welcome, {username}
                """)
                logged_in = True
                while True:
                    show_menu()
                    option =  option_choose([1,2,3],"Enter choice:- ","Please enter a valid choice")
                    if option == 1:
                        print("Home")
                    elif option == 2:
                        oldPwd = get_input("Entre your old password:- ","Please enter an old password")
                        if oldPwd == user["password"]:
                            newPwd =  get_input("Entre your new password:- ","Please enter an new password")
                            user["password"]=newPwd
                            print("Password changed successfully")
                            print("Home")
                        else:
                            print("Wrong Password") 
                    elif option == 3:
                        logged_in = False
                        break  
            else:
                    print("wrong credentials")
            
        else:
            print( "Please register first")
    elif choice == 3:
        print("Goodbye!")
        break
    # else:
    #  print("Invalid choice!")
