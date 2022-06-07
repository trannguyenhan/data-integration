import csv
from engine import EngineInterface

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

            sample = next(reader)
            while len(sample) != len(self.header) or sample == None: 
                sample = next(reader)
            
            self.header = super().extract_header()
            for it in range(0, len(self.header)): 
                if self.header[it] not in self.data_sample: 
                    self.data_sample[self.header[it]] = sample[it]

        return super().extract_header()

    def dump_data_to_warehouse():
        pass

if __name__ == "__main__": 
    engine = EngineCsv("/home/trannguyenhan/dataset/ign.csv", True)
    schema = engine.extract_schema()
    print(schema)