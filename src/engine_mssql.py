from engine_mysql import EngineMysql
import pyodbc

class EngineMssql(EngineMysql): 
    def load_data_source(self):
        self.db = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server},SERVER='
                +self.hostName+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password
        )

    def dump_data_to_warehouse():
        pass

if __name__ == "__main__": 
    engine = EngineMssql("localhost", "sa", "Helloworld123", "test_database", "users")
    schema = engine.extract_schema()
    print(schema)
    # engine.extract_header()
    # print(engine.header)