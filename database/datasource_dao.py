from utils import Context
from . import db

def add(type):
    Context.project["data sources"].append({
        "type": type,
        "connection string": "",
        "schema": {},
        "mapping": {}
    })
    db.updateById(Context.project["id"], Context.project)

def remove_at(idx):
    Context.project['data sources'].pop(idx)
    db.updateById(Context.project["id"], Context.project)

def save():
    db.updateById(Context.project["id"], Context.project)
