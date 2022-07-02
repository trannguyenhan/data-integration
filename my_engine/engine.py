from utils.helpers import fill_none_value_header, standardization_data_type, pre_convert, most_common

class EngineInterface():
    SIZE_SAMPLE_DATA = 10

    def __init__(self, path_file):
        self.path_file = path_file
        self.data_sample = {}
        self.file = None
        self.header = []
        self.num_header = 0

    def load_data_source(self):
        try: 
            self.file = open(self.path_file)
            return self.file
        except: 
            print("Error when load file from source!")
            return None

    # extract header and add data sample to self.header
    # data sample is suggest data type of header
    def extract_header(self):
        self.header = fill_none_value_header(self.header)
        return self.header

    # return dictionary map field name with data type 
    def extract_schema(self):
        self.extract_header()
        if len(self.header) == 0: 
            self.extract_header()
        
        schema = {}
        for k in self.data_sample: 
            v = self.data_sample[k]
            schema[k] = standardization_data_type(type(v).__name__)

        return schema
    
    def get_sample_data(self):
        self.extract_header()
        return [self.data_sample]

    def extract_schema_v2(self):
        data = self.get_sample_data()
        
        schema = {}
        for item in data: 
            for k in item: 
                v = item[k]
                if k not in schema: 
                    schema[k] = []
                else: 
                    vtemp = pre_convert(v)
                    schema[k].append(standardization_data_type(type(vtemp).__name__))

        newSchema = {}
        for item in schema: 
            value = schema[item]
            newValue = most_common(value)
            newSchema[item] = newValue
        
        return newSchema