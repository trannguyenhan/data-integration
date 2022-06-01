from helpers import fill_none_value_header

class EngineInterface():
    def __init__(self, path_file, is_header = True):
        self.path_file = path_file
        self.is_header = is_header
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