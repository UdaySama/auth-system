logged_in= True

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
show_menu()