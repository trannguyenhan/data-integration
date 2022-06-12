import engine.engine_mongodb

# dump data to warehouse
# when dump to warehouse, identify of each proj is proj_name
# so, we want get data of proj using proj_name
# if you want change warehouse storage -> change your engine
def dump(data, proj_name):
    engine.engine_mongodb.EngineMongodb.save_data(data, proj_name)

# if you want change warehouse storage -> change your engine
def delete(proj_name): 
    engine.engine_mongodb.EngineMongodb.drop_proj_warehouse(proj_name)