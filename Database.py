import sqlite3

# Connect to or create an SQLite database file
connection, cursor 

def main():
    ...
def connect(db_name):
    global connection, cursor
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()



if __name__ == "__main__":
    main()