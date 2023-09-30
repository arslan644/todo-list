import Database
import utilities as u
import time 

def get_username():
    return input("Username: ")

def get_password():
    return input("Password: ")

def signup_user():
    get_credentials()

def login_user():
    try:
        username = get_username()
        while not username_exist(username):
            u.printColoredText("Invalid Username", "red")
            time.sleep(1)
            return False
        password = get_password()
        while not password_match(username, password):
            u.printColoredText("Password does not match", "red")
            time.sleep(1)
            return False
    except Exception as e:
        print(e)
        login_user()
    return True

def username_exist(username):
    return Database.record_exist("Users", "username", username)

def password_match(username, password):
    return Database.record_match("Users", "username", username, "password", password)