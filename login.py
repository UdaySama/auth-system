def get_input(message,error_Msg):
    value = input(message)
    value=value.strip()
    while not value:
        print(error_Msg)
        value = input(message)
        value=value.strip()
    return value

def register():
    username = get_input("Entre Username:- ", "Please enter a username")
    password = get_input("Entre Password:- ", "Please enter a Password")
    user ={
        "username":username,
        "password":password
    }
    return user



def login(user):
    username = get_input("Entre Username:- ", "Please enter a username")
    password = get_input("Entre Password:- ", "Please enter a Password")
    if username == user["username"] and password == user["password"]:
        return True
    else:
        return False


user = {
    "username": "parvej",
    "password": "12345"
}

result = login(user)
print(result)