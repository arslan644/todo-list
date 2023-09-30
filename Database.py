import sqlite3, utilities

connection = None
cursor  = None

def main():
    a = "AUTOINCREMENT"
    f = "FOREIGN KEY "
    i = "INTEGER"
    n = "NOT NULL"
    p = " PRIMARY KEY"
    r = "REFERENCES "
    s = "SELECT"
    t = "TEXT"
    u = "UNIQUE"
    table_name = "Users"
    data = {"id": f"{i} {p} {a}", "username": f"{t} {u} {n}"}
    connect("TODO")
    #drop_table(table_name)
    create_table(table_name, data)
    #insert_data(table_name, data)
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

def column_exist(table_name, column_name):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    column_names = [col[1] for col in columns]
    return column_name in column_names

def record_exist(table_name, column_name, value_to_check):
    if table_exist(table_name) and column_exist(table_name, column_name):
        cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name}=?", (value_to_check,))
        result = cursor.fetchone()
        return result is not None
    else:
        create_table(table_name)

def table_size(name):
    cursor.execute(f"SELECT count(*) FROM {name};")
    size = cursor.fetchone()
    return size[0]

#name paramter is the name of the table and columns parameter is a dictionary having keys as names of column in string and value
def create_table(name, columns={}) -> None:
    """
        create_table(string, {"columnName": "DataType Attributes"}) -> None

        Call this method for creating a table of given name as string and
        column data as a dictionary with keys as column names in string and
        Value as a space separated string of words, first word is datatype of column
        and following words are for other attributes if any.
        
        :param name: Name of the table to be created.
        :type name: String
        :param columns: Keys as column names and values as datatypes and attributes.
        :type columns: Dictionary 
        
        ➡
        """
    
    query = f"CREATE TABLE IF NOT EXISTS {name} "
    if len(columns) == 0:
        cursor.execute(f'''{query} (dummy_column INTEGER)''')
    else:
        cols = ""
        keys = list(columns.keys())
        for i in range(len(columns)):
            col_name = keys[i]
            col_type_attributes = columns[col_name]
            cols += f'''{col_name} {col_type_attributes} , '''
        cols = utilities.remove_last_occurence(cols, ",")
        query += f'''({cols})'''
        cursor.execute(query)

def drop_table(name):
    query = f"DROP TABLE IF EXISTS {name}"
    cursor.execute(query)

def insert_data(tableName, data={}):
    keys = list(data.keys())
    names = utilities.list_to_string(keys)
    placeholders = f"{'?, ' * len(keys)}"
    placeholders = utilities.remove_last_occurence(placeholders, ", ")
    values = tuple(data.values())
    query = f"INSERT INTO {tableName} ({names}) VALUES ({placeholders})"
    cursor.execute(query, values)

def commit():
    connection.commit()

def close():
    connection.close()

if __name__ == "__main__":
    main()