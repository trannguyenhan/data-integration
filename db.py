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
