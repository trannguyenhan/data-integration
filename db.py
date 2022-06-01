import sqlite3

class Database:
    def __init__(self):
        raise Exception("This class cannot instantiate")

    con = sqlite3.connect('data/data.db')

    try:
        con.execute('CREATE TABLE projects (project_id INTEGER PRIMARY KEY AUTOINCREMENT, \
                                                    project_name text NOT NULL)')

        print("Database initialized")
    except sqlite3.OperationalError:
        print("Database connected")