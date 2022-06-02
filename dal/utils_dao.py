'''
Others DAO
'''

from db import Database as db

def get_all_table():
    return db.con.execute("SELECT name FROM sqlite_schema").fetchall()

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
    db.con.execute(query)
    db.con.commit()
    print("created table")



