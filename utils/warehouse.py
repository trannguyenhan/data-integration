from my_engine.engine_mongodb import EngineMongodb

from utils.constants import SourceType


# dump data to warehouse
# when dump to warehouse, identify of each proj is proj_name
# so, we want get data of proj using proj_name
# if you want change warehouse storage -> change your engine
def dump(data, proj_name):
    EngineMongodb.save_data(data, proj_name)

# if you want change warehouse storage -> change your engine
def delete(proj_name): 
    EngineMongodb.drop_proj_warehouse(proj_name)

# lst is list engine was init
'''
    lst: 
        {
            "engine": engine_csv,
            "mapping_target": {
                "url": "URL",
                "column1": "convert_column1"
            }
        }
    proj_name: proj5
'''
def dump_with_engine(lst, proj_name, dest_type, deduplicate, path_name = None, \
                        host = None, username = None, password = None, database = None, tableName = None):
    schema_dest = []

    cnt = 0

    for item in lst: 
        engine = item['engine']
        mapping_target = item['mapping_target']
        engine.dump_data_to_warehouse(mapping_target, proj_name)

        if cnt == 0: 
            for mapping_item in mapping_target: 
                schema_dest.append(mapping_target[mapping_item])
        cnt += 1

    if deduplicate:
        EngineMongodb.remove_duplicate(proj_name)

    if dest_type == SourceType.XML: 
        EngineMongodb.to_xml(proj_name, schema_dest, path_name)
    elif dest_type == SourceType.CSV: 
        EngineMongodb.to_csv(proj_name, schema_dest, path_name)
    elif dest_type == SourceType.JSON: 
        EngineMongodb.to_json(proj_name, schema_dest, path_name)
    elif dest_type == SourceType.MySQL: 
        EngineMongodb.to_mysql(proj_name, schema_dest, host, username, password, database, tableName)
    else:
        raise Exception(f"Dest type {dest_type} not supported yet")