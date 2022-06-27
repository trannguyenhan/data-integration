from asyncore import read
import csv
from . import EngineInterface
import utils.warehouse
from utils.constants import SourceType
import pandas as pd

class EngineCsv(EngineInterface): 
    def __init__(self, path_file, delimiter = ",", type_file = SourceType.CSV):
        self.delimiter = delimiter
        self.typeFile = type_file

        if self.typeFile == SourceType.EXCEL:
            file_excel_tmp = pd.read_excel(path_file)
            new_csv_file_name = path_file + ".csv" # example file name is test.xlsx.csv
            file_excel_tmp.to_csv(new_csv_file_name, index=None, header=True)
            path_file = new_csv_file_name
            
        super().__init__(path_file)

    # extract header of csv file
    def extract_header(self, is_header = True):
        self.load_data_source()
        if self.file != None: 
            reader = csv.reader(self.file, delimiter=self.delimiter)
            
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
            reader = csv.reader(self.file, delimiter=self.delimiter)

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
                try:
                    line = next(reader)
                except:
                    return result
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
            reader = csv.reader(self.file, delimiter=self.delimiter)
            
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