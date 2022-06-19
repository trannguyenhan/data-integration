from asyncore import read
import csv
from . import EngineInterface
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

    def get_sample_data(self):
        self.extract_header()
        if len(self.header) == 0: 
            return []
        

        result = []
        self.load_data_source()
        if self.file != None: 
            reader = csv.reader(self.file)

            line = next(reader) # ignore header
            line = next(reader)

            cnt = 0
            while cnt < self.SIZE_SAMPLE_DATA: 
                resultItem = {}

                lens = len(line)
                for i in range(0, lens): 
                    k = self.header[i]
                    v = line[i]
                    resultItem[k] = v
                
                result.append(resultItem)
                line = next(reader)
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
                    k = self.header[i]    # get key from header
                    if k in mapping_target: # check header in header mapping
                        v = line[i]             # get value from each line csv reader
                        resultItem[mapping_target[k]] = v

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