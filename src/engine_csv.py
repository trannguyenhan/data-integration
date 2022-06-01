import csv
from engine import EngineInterface
import pandas as pd

class EngineCsv(EngineInterface): 

    # extract header of csv file
    def extract_header(self):
        self.load_data_source()
        if self.file != None: 
            reader = csv.reader(self.file)
            
            if(self.is_header == True): 
                self.header = next(reader)
            else: 
                tmp = next(reader)
                for it in range(0, len(tmp)): 
                    self.header.append(None)

        return super().extract_header()
        

    # return dictionary map name with data type 
    def extract_schema(self):
        if len(self.header) == 0: 
            self.extract_header()
        
        schema = {}
        data = pd.read_csv(self.file, header=None).dtypes.to_list()
        
        lens = len(self.header)
        for item in range(0,lens): 
            name = self.header[item]
            datatype = data[item]
            schema[name] = str(datatype)

        return schema
    
    

    def dump_data_to_warehouse():
        pass

if __name__ == "__main__": 
    engine = EngineCsv("/home/trannguyenhan/dataset/ign.csv", True)
    engine.extract_schema()