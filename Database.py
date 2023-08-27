import sqlite3, utilities

connection = None
cursor  = None

def main():
    i = "INTEGER"
    p = " PRIMARY KEY"
    t = "TEXT"
    f = "FOREIGN KEY "
    r = "REFERENCES "
    table_name = "Users"
    data = {"username": "arno", "password": "testing"}
    connect("TODO")
    insert_data(table_name, data)
    commit()
    close()

def connect(db_name):
    global connection, cursor
    connection = sqlite3.connect(f"{db_name}.db")
    cursor = connection.cursor()

def table_exist(name):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}'")
    result = cursor.fetchone()
    return result[0] is not None

def table_size(name):
    cursor.execute(f"SELECT count(*) FROM {name};")
    size = cursor.fetchone()
    return size[0]

def create_table(name, columns={}):
    query = f"CREATE TABLE IF NOT EXISTS {name} "
    if len(columns) == 0:
        cursor.execute(f'''{query} (dummy_column INTEGER)''')
    else:
        cols = ""
        keys = list(columns.keys())
        for i in range(len(columns)):
            col_name = keys[i]
            col_type = columns[col_name]
            cols += f'''{col_name} {col_type}, '''
        cols = utilities.remove_last_occurence(cols, ",")
        query += f'''({cols})'''
        cursor.execute(query)

def drop_table(name):
    query = f"DROP TABLE IF EXISTS {name}"
    cursor.execute(query)

def insert_data(name, data={}):
    keys = list(data.keys())
    names = utilities.list_to_string(keys)
    placeholders = f"{'?, ' * len(keys)}"
    placeholders = utilities.remove_last_occurence(placeholders, ", ")
    values = tuple(data.values())
    query = f"INSERT INTO {name} ({names}) VALUES ({placeholders})"
    cursor.execute(query, values)

def commit():
    connection.commit()

def close():
    connection.close()

if __name__ == "__main__":
    main()