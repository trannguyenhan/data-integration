from utils import Context
from . import db

# def update_ctx():
#     Context.project = db.getById(Context.project['id'])

def add(type):
    Context.project["data sources"].append({
        "type": type,
        "connection string": "",
        "schema": {},
        "mapping": {}
    })
    db.updateById(Context.project["id"], Context.project)
    # update_ctx()

def remove_at(idx):
    Context.project['data sources'].pop(idx)
    db.updateById(Context.project["id"], Context.project)