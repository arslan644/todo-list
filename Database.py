import sqlite3, utilities

connection = None
cursor  = None

def main():
    table_name = "Lists"
    connect("TODO")
    commit()
    close()

def connect(db_name):
    global connection, cursor
    connection = sqlite3.connect(f"{db_name}.db")
    cursor = connection.cursor()

def table_exist(table_name):
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    result = cursor.fetchone()
    return result[0] is not None

def table_size(table_name):
    cursor.execute(f"SELECT count(*) FROM {table_name};")
    size = cursor.fetchone()
    return size[0]

def create_table(name, columns={}):
    query = f"CREATE TABLE {name} "
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

def commit():
    connection.commit()

def close():
    connection.close()

if __name__ == "__main__":
    main()