from utils.constants import DataType, SourceType
import os
import re
import mysql
import pyodbc


def fill_none_value_header(header):
    cnt = 1

    new_header = []
    for item in header:
        new_item = item
        if item == None or item == "":
            name_column = "col" + str(cnt)
            cnt += 1
            new_item = name_column
        new_header.append(new_item)

    return new_header


def get_db_connection(con_string):
    host, user, password, database, table = con_string.split(';')
    host = host.split("=")[1].strip()
    user = user.split("=")[1].strip()
    password = password.split("=")[1].strip()
    database = database.split("=")[1].strip()
    table = table.split("=")[1].strip()
    return host, user, password, database, table
# convert data type from everything to list data type standardization

# include: object, string, integer, float, date, boolean


def standardization_data_type(data_type):
    if data_type in DataType.ALL:
        return data_type
    elif data_type == "str":
        return DataType.STR
    elif data_type == "float":
        return DataType.FLOAT
    elif data_type == "int":
        return DataType.INT
    elif data_type == "bool":
        return DataType.BOOL
    elif data_type == "datetime.date" or data_type == "datetime":
        return DataType.DATE
    return DataType.STR


def check_connection(source_type, connection_string):
    '''
        Return (check: boolean, message: string)
    '''

    valid_extension = {
        SourceType.TXT: ['txt'],
        SourceType.CSV: ['csv'],
        SourceType.EXCEL: ['xls', 'xlsx'],
        SourceType.JSON: ['json'],
        SourceType.XML: ['xml']
    }

    if source_type in SourceType.FILE:
        if not os.path.exists(connection_string):
            return False, "File is not exist"
        if not re.match(f".*\.({'|'.join(valid_extension[source_type])})", connection_string):
            return False, f"File extension must in [{','.join(valid_extension[source_type])}]"
    elif source_type == SourceType.MySQL:
        try:
            host, user, password, database, table_name = get_db_connection(connection_string)
            con = mysql.connector.connect(host=host, user=user, password=password, database=database)
            con.disconnect()
        except Exception as e:
            return False, "Connect to MySQL failed. Error: " + str(e)
    elif source_type == SourceType.MSSQL:
        try:
            host, user, password, database, table_name = get_db_connection(connection_string)
            con = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host};DATABASE={database};UID={user};PWD={password}")
            con.close()
        except Exception as e:
            return False, "Connect to MSSQL failed. Error: " + str(e)
    else:
        raise Exception(f"Source type {source_type} is not supported")

    return True, "Test OK"