from . import EngineInterface
import pyodbc

class EngineMssql(EngineInterface): 
    def __init__(self, host_name, username, password, database, table_name):
        self.hostName = host_name
        self.username = username
        self.password = password
        self.database = database
        self.tableName = table_name

        self.db = None
        super().__init__(None)

    def load_data_source(self):
        self.db = pyodbc.connect(
            'DRIVER={SQL Server Native Client 17.0},SERVER='
                +self.hostName+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password
        )
    
    def extract_header(self):
        self.load_data_source()

        mcursor = self.db.cursor()
        mcursor.execute("Select * from " + self.tableName + " limit 1")
        resultSample = mcursor.fetchone()

        self.header = [i[0] for i in mcursor.description]
        cnt = 0
        for field_name in self.header: 
            self.data_sample[field_name] = resultSample[cnt]
            cnt += 1

        mcursor.close()
        return self.header
    
    def dump_data_to_warehouse(self, header_target):
        self.extract_header()
        if len(self.header) != len(header_target): # (1)
            # schema source not fit with schema destination
            return False

        # load again data source
        result = []

        self.load_data_source()
        

if __name__ == "__main__": 
    engine = EngineMssql("localhost", "sa", "Helloworld123", "test_database", "users")
    schema = engine.extract_schema()
    print(schema)
    # engine.extract_header()
    # print(engine.header)