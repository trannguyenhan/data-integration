import utils.warehouse
from . import EngineInterface
import mysql.connector
import utils.helpers

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

    def extract_header(self):
        self.load_data_source()

        mcursor = self.db.cursor()
        mcursor.execute("Select * from " + self.tableName + " limit 1")
        resultSample = mcursor.fetchone()

        self.header = [i[0] for i in mcursor.description]
        cnt = 0
        for field_name in self.header: 
            if resultSample != None:
                self.data_sample[field_name] = resultSample[cnt]
            cnt += 1

        mcursor.close()
        return self.header

    def get_sample_data(self):
        self.extract_header()
        if len(self.header) == 0: 
            return []
        
        # when load header file is close
        # load again data source
        result = []
        self.load_data_source()
        if self.db != None: 
            mcursor = self.db.cursor()
            mcursor.execute("Select * from " + self.tableName)
            fetchResult = mcursor.fetchall()
            
            if(fetchResult == None):
                return []

            cnt = 0
            for item in fetchResult: 
                if cnt >= self.SIZE_SAMPLE_DATA: 
                    break

                resultItem = {}
                cntItem = 0
                for v in item: 
                    resultItem[self.header[cntItem]] = v
                    cntItem += 1

                result.append(resultItem)
                cnt += 1
            
            return result
        
        # resource not found
        return []


    def dump_data_to_warehouse(self, mapping_target, proj_name):
        self.extract_header()
        if len(mapping_target) == 0:
            return False

        # load again data source
        result = []

        self.load_data_source()
        if self.db != None: 
            mcursor = self.db.cursor()
            mcursor.execute("Select * from " + self.tableName)
            fetchResult = mcursor.fetchall()

            for item in fetchResult: 
                resultItem = {}
                cnt = 0
                
                for v in item: 
                    k = self.header[cnt]
                    if k in mapping_target: 
                        resultItem[mapping_target[k]] = utils.helpers.after_convert(v)
                    cnt += 1

                result.append(resultItem)
                
            utils.warehouse.dump(result, proj_name)
            return True
        
        # not connect to resource
        return False

if __name__ == "__main__": 
    engine = EngineMysql("localhost", "root", "mysql12345", "foodapi", "orders")
    schema = engine.extract_schema()
    print(schema)
    # engine.extract_header()
    # print(engine.header)