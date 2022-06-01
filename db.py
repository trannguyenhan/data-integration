import sqlite3

class Database:
    def __init__(self):
        raise Exception("This class cannot instantiate")

    con = sqlite3.connect('data/data.db')

    # Check if database is existed or not. If not, initialize it by execute script in `init_db.sql` 
    try:
        sql_file = open("init_db.sql")
        sql_as_string = sql_file.read()
        con.executescript(sql_as_string)
        print("Database initialized")
    except sqlite3.OperationalError:
        print("Database connected")


    def create_table(table_name, columns):
        '''
        Creata a table with specifics columns.
        columns is a list of tuple, example:
        columns = [('ID', 'integer'), ('Name', 'string'), ('Date of birth', 'date'), ('GPA', 'float')]
        '''
        dtype_map = {"integer": "INTEGER", "string": "TEXT", "date": "date", "float": "real"}
        query = f'CREATE TABLE [{table_name}] ('
        for i, (cl_name, dtype) in enumerate(columns):
            sql_dtype = dtype_map[dtype]
            query += f'{cl_name} {sql_dtype}'
            if i != len(columns) - 1:
                query += ','
        query += ')'

        print("Query: ", query)
        Database.con.execute(query)
        Database.con.commit()
        print("created table")