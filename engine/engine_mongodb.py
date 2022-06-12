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

    @staticmethod
    def save_data(data, project_name_dest):
        # this case we will dump data to my warehouse
        # so, not need user enter them database, we will use our database
        # and need user enter name of project, we will use project name is name of collection
        engine = EngineMongodb("localhost", "", "", "datawarehouse", project_name_dest)               
        engine.load_data_source()

        if isinstance(data, list): 
            # ex: [{"data": 1, "beta": 2}]
            engine.db.insert_many(data)
        else: 
            #ex: {"data": 1, "beta": 2}
            engine.db.insert_one(data)

    @staticmethod
    def drop_proj_warehouse(project_name_dest):
        engine = EngineMongodb("localhost", "", "", "datawarehouse", project_name_dest)               
        engine.load_data_source()
        engine.db.drop()

if __name__ == "__main__": 
    engine = EngineMongodb("localhost", "", "", "X-news", "news")
    # engine.extract_header()
    # print(engine.header)
    schema = engine.extract_schema()
    print(schema)