from . import EngineInterface
import json
import utils.warehouse
import utils.helpers

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
    def dump_data_to_warehouse(self, mapping_target, proj_name):
        self.extract_header()
        if len(mapping_target) == 0: 
            return False

        # load again data source
        result = []

        self.load_data_source()
        if self.file != None: 
            reader = json.load(self.file)

            for item in reader: 
                resultItem = {}

                # item is dict = (k,v)
                # replace new key -> header_target[i]
                for k in item:
                    if k in mapping_target:  # check header in header mapping
                        resultItem[mapping_target[k]] = utils.helpers.after_convert(item[k])
                    # only map header in mapping target and dump it to mongodb

                result.append(resultItem)
            
            utils.warehouse.dump(result, proj_name)
            return True
    
        # file not found
        return False

if __name__ == "__main__": 
    engine = EngineJson("/home/trannguyenhan/dataset/alonhadat/house_price_prediction.json")
    schema = engine.extract_schema()
    
    print(schema)