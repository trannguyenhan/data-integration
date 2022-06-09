'''
Project "data access object"
'''

from database import db

def get_project_list():
    return db.getAll()

def get_by_name(prj_name):
    matches = db.getBy({"project name": prj_name})
    if len(matches) == 0:
        raise Exception("Not found any project with name" + prj_name)
    return matches[0]

def add_new_project(prj_name, destination_type):
    if len(db.getBy({"project name": prj_name})) > 0:
        raise Exception("Duplicate project name")

    db.add({
        "project name": prj_name, 
        "destination type": destination_type,
        "connection string": None,
        "is initialized": False,
        "destination schema": None,
        "data sources": []
    })


def update_is_initialized(prj_name, bool):
    db.update({"project name": prj_name}, {"is initialized": bool})

def set_connection_str(prj_name, conn_str):
    db.update({"project name": prj_name}, {"connection string": conn_str})

def set_destination_schema(prj_name, dest_schema):
    db.update({"project name": prj_name}, {"destination schema": dest_schema})

def delete(prj_name):
    project = get_by_name(prj_name)
    db.deleteById(project['id'])