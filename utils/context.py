class Context:
    '''A class which saves info of a working session'''

    def __init__(self):
        raise Exception("Context class cannot be instantiated")
    
    # Current working project
    project = None

    # Current working data source (will be use in window "config_file")
    data_source = None