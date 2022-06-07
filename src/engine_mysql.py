from engine import EngineInterface
import mysql.connector

class EngineMysql(EngineInterface): 
    def __init__(self, host_name, username, password, database, table_name):
        self.hostName = host_name
        self.username = username
        self.password = password
        self.database = database
        self.tableName = table_name

        self.db = None
        super().__init__(None)

    def load_data_source(self):
        self.db = mysql.connector.connect(
            host = self.hostName,
            user = self.username,
            password = self.password,
            database = self.database
        )

        self.tableName = self.tableName


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

        return self.header

    def dump_data_to_warehouse():
        pass

if __name__ == "__main__": 
    engine = EngineMysql("localhost", "root", "mysql12345", "foodapi", "orders")
    schema = engine.extract_schema()
    print(schema)
    # engine.extract_header()
    # print(engine.header)