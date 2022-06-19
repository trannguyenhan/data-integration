from . import EngineInterface
import json
import utils.warehouse

class EngineJson(EngineInterface):
    def extract_header(self):
        self.load_data_source()
        if self.file != None:
            reader = json.load(self.file)
            json_header = set()

            for item in reader: 
                for k in item: 
                    json_header.add(k)
                    if k not in self.data_sample: 
                        self.data_sample[k] = item[k]

        self.header = list(json_header)
        self.file.close()
        return self.header

    def get_sample_data(self):
        self.extract_header()
        if len(self.header) == 0: 
            return []
        
        result = []
        self.load_data_source()
        
        if self.file != None: 
            reader = json.load(self.file)
            
            cnt = 0
            for item in reader: 
                if cnt >= self.SIZE_SAMPLE_DATA: 
                    break

                resultItem = {}
                for k in item: 
                    resultItem[k] = item[k]
                
                result.append(resultItem)
                cnt += 1
            
            return result
        
        # file not found
        return []

    # dump data to warehouse -> mongodb
    def dump_data_to_warehouse(self, header_target, proj_name):
        self.extract_header()
        if len(self.header) != len(header_target): # (1)
            # schema source not fit with schema destination
            return False

        # load again data source
        result = []

        self.load_data_source()
        if self.file != None: 
            reader = json.load(self.file)

            for item in reader: 
                resultItem = {}

                cnt = 0
                # item is dict = (k,v)
                # replace new key -> header_target[i]
                for k in item: 
                    resultItem[header_target[cnt]] = item[k]
                    cnt += 1
                
                result.append(resultItem)
            
            utils.warehouse.dump(result, proj_name)
            return True
    
        # file not found
        return False

if __name__ == "__main__": 
    engine = EngineJson("/home/trannguyenhan/dataset/alonhadat/house_price_prediction.json")
    schema = engine.extract_schema()
    
    print(schema)