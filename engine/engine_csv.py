import csv
from engine.engine import EngineInterface
import utils.warehouse

class EngineCsv(EngineInterface): 

    # extract header of csv file
    def extract_header(self, is_header = True):
        self.load_data_source()
        if self.file != None: 
            reader = csv.reader(self.file)
            
            if(is_header == True): 
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
        
        self.file.close()
        return super().extract_header()

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
            reader = csv.reader(self.file)
            
            line = next(reader) # ignore header
            line = next(reader)
            
            while line != None: 
                # line is array: list of value
                resultItem = {}

                # for header_target
                # for line
                # len(line) and len(header_target) is same (check in (1))
                lens = len(line)
                for i in range(0, lens): 
                    k = header_target[i]    # get key from header target
                    v = line[i]             # get value from each line csv reader
                    resultItem[k] = v

                result.append(resultItem)
                line = next(reader, None)

            utils.warehouse.dump(result, proj_name)
            return True

        # file not found
        return False


if __name__ == "__main__": 
    engine = EngineCsv("/home/trannguyenhan/dataset/ign.csv")
    schema = engine.extract_schema()
    print(schema)