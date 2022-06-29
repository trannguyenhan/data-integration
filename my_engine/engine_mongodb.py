import csv
import json
import xml.etree.ElementTree as ET
from pydoc import doc

from pymongo import mongo_client
from utils.deduplicate_mongo import find_duplicate

from . import EngineInterface


class EngineMongodb(EngineInterface): 
    def __init__(self, host_name, username, password, database, table_name):
        self.hostName = host_name
        self.username = username
        self.password = password
        self.database = database
        self.tableName = table_name

        self.db = None
        super().__init__(None)
        
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

    @staticmethod
    def to_csv(project_name_dest, schema_dest):
        engine = EngineMongodb("localhost", "", "", "datawarehouse", project_name_dest)
        engine.load_data_source()
        cursor = engine.db.find({})

        csv_output_file = open(project_name_dest + ".csv", "w")
        csv_writer = csv.writer(csv_output_file)
        headers = []

        cnt = 0
        for document in cursor: 
            line = []
            if cnt == 0: 
                for item in document: 
                    if item in schema_dest: 
                        headers.append(item)
                        line.append(document[item])
                
                        if cnt == 0: 
                            csv_writer.writerow(headers)
                        csv_writer.writerow(line)
            else: 
                for item in document: 
                    if item in schema_dest: 
                        line.append(document[item])
                        csv_writer.writerow(line)
            
            cnt += 1

        csv_output_file.close()
    @staticmethod
    def remove_duplicate(project_name_dest):
        engine = EngineMongodb("localhost", "", "", "datawarehouse", project_name_dest)
        engine.load_data_source()
        list_ids_dup = find_duplicate(engine.db)
        result = engine.db.delete_many({"_id": {'$in': list_ids_dup}})
        print(result)
    
    @staticmethod
    def to_json(project_name_dest, schema_dest):
        engine = EngineMongodb("localhost", "", "", "datawarehouse", project_name_dest)
        engine.load_data_source()
        cursor = engine.db.find({})

        result = []
        for document in cursor: 
            newDocument = {}
            for item in document: 
                if item in schema_dest:
                    newDocument[item] = document[item]
            
            result.append(newDocument)

        json_object = json.dumps(result)
        with open(project_name_dest + ".json", "w") as output_file: 
            output_file.write(json_object)
    
    @staticmethod
    def to_xml(project_name_dest, schema_dest):
        engine = EngineMongodb("localhost", "", "", "datawarehouse", project_name_dest)
        engine.load_data_source()
        cursor = engine.db.find({})

        tree = ET.ElementTree("tree")

        root = ET.Element('data')
        for document in cursor: 
            subRoot = ET.SubElement(root, "sub-root")
            for item in document: 
                if item in schema_dest:
                    xmlItem = ET.SubElement(subRoot, item)
                    # all value element xml is string -> convert to string
                    xmlItem.text = str(document[item]) 
        
        tree._setroot(root)
        tree.write(project_name_dest + ".xml", encoding="utf-8", xml_declaration=True)

    @staticmethod
    def to_mysql(project_name_dest, schema_dest):
        engine = EngineMongodb("localhost", "", "", "datawarehouse", project_name_dest)
        engine.load_data_source()
        cursor = engine.db.find({})

        

if __name__ == "__main__": 
    engine = EngineMongodb("localhost", "", "", "X-news", "news")
    # engine.extract_header()
    # print(engine.header)
    schema = engine.extract_schema()
    print(schema)
