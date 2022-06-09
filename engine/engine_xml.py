from engine.engine import EngineInterface

class EngineXml(EngineInterface): 

    def extract_header(self):
        self.load_data_source()

        return super().extract_header()

    def dump_data_to_warehouse():
        pass

if __name__ == "__main__": 
    engine = EngineXml("/home/trannguyenhan/dataset/ign.csv", True)
    schema = engine.extract_schema()
    print(schema)