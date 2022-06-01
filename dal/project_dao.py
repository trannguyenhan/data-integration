'''
Project "data access object"
'''

from db import Database as db

def get_project_list():
    return db.con.execute("SELECT * FROM projects").fetchall()

def add_new_project(name, destination):
    db.con.execute(f"INSERT INTO projects (project_name, destination) VALUES (?, ?)", (name, destination))
    db.con.commit()