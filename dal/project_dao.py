'''
Project "data access object"
'''

from db import Database as db

def get_project_list():
    return db.con.execute("SELECT * FROM projects").fetchall()

def add_new_project(name, destination):
    db.con.execute(f"INSERT INTO projects (project_name, destination) VALUES (?, ?)", (name, destination))
    db.con.commit()

def set_is_initialized_to_true(project_id):
    db.con.execute(f"UPDATE projects SET is_initialized = 1 WHERE project_id=?", (project_id,))
    db.con.commit()

def get_project_by_id(id):
    return db.con.execute(f"SELECT * FROM projects WHERE project_id=?", (id,)).fetchone()

def set_connection_str(id, conn_str):
    db.con.execute(f"UPDATE projects SET connection_str = ? WHERE project_id = ?", (conn_str, id))
    db.con.commit()