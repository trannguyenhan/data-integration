from engine.engine_mysql import EngineMysql
from pymongo import mongo_client

class EngineMongodb(EngineMysql): 
    def load_data_source(self):
        client = mongo_client.MongoClient(self.hostName, 27017)
        self.db = client[self.database][self.tableName]

    def extract_header(self):
        self.load_data_source()

        data = self.db.find()
        self.data_sample = data[0]

        for item in data[0]: 
            self.header.append(item)

        return self.header

    def dump_data_to_warehouse():
        pass

if __name__ == "__main__": 
    engine = EngineMongodb("localhost", "", "", "X-news", "news")
    # engine.extract_header()
    # print(engine.header)
    schema = engine.extract_schema()
    print(schema)