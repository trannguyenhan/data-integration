from helpers import fill_none_value_header
import pandas as pd

class EngineInterface():
    def __init__(self, path_file, is_header = True):
        self.path_file = path_file
        self.is_header = is_header
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

    def extract_header(self):
        self.header = fill_none_value_header(self.header)
        return self.header

    # return dictionary map name with data type 
    def extract_schema(self):
        if len(self.header) == 0: 
            self.extract_header()
        
        schema = {}
        for k in self.data_sample: 
            v = self.data_sample[k]
            schema[k] = type(v).__name__

        return schema
