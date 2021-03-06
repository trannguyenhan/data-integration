class DataType: 
    OBJ = "object"
    INT = "integer"
    STR = "string"
    DATE = "date"
    FLOAT = "float"
    BOOL = "boolean"

    ALL = [OBJ, INT, STR, DATE, FLOAT, BOOL]


class SourceType:
    XML = "XML"
    TXT = "TXT"
    JSON = "JSON"
    EXCEL = "EXCEL"
    CSV = "CSV"
    MySQL = "MySQL"
    MSSQL = "MS SQL Server"

    ALL = [XML, TXT, JSON, EXCEL, CSV, MySQL, MSSQL]
    FILE = [XML, TXT, JSON, EXCEL, CSV]
    DATABASE = [MySQL, MSSQL]
