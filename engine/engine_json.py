from engine.engine import EngineInterface
import json

class EngineJson(EngineInterface):
    def extract_header(self):
        self.load_data_source()
        if(self.file != None):
            reader = json.load(self.file)
            json_header = set()

            for item in reader: 
                for k in item: 
                    json_header.add(k)
                    if k not in self.data_sample: 
                        self.data_sample[k] = item[k]

        self.header = list(json_header)
        return self.header

    
if __name__ == "__main__": 
    engine = EngineJson("/home/trannguyenhan/dataset/alonhadat/house_price_prediction.json")
    schema = engine.extract_schema()
    
    print(schema)