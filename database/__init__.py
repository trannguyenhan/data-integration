import pysondb

class Database:
    def __init__(self):
        raise Exception("This class cannot instantiate")

    # Connect to json file
    db_path = "database/data/data.json"
    db = pysondb.db.getDb(db_path)
    print("Connected database:", db_path)

db = Database.db