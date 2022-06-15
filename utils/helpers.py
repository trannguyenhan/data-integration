from utils.constants import DataType

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

# convert data type from everything to list data type standardization
# include: object, string, integer, float, date, boolean
def standardization_data_type(data_type):
    if data_type in DataType.ALL: 
        return data_type
    elif data_type == "str":
        return  DataType.STR
    elif data_type == "float":
        return DataType.FLOAT
    elif data_type == "int":
        return DataType.INT
    elif data_type == "bool":
        return DataType.BOOL
    elif data_type == "datetime.date":
        return DataType.DATE
    return data_type