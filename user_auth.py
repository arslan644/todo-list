import Database

def get_username():
    return input("Username: ")

def get_password():
    return input("Password: ")

def signup_user():
    get_credentials()

def login_user():
    try:
        if not username_exist(get_username()):
            print("Invalid Username")
    except Exception:
        login_user()

def username_exist(username):
    return Database.record_exist("Users", "username", username)

