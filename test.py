# this is file test engine

import engine.engine, engine.engine_csv, engine.engine_json, engine.engine_mssql, engine.engine_mysql, engine.engine_xml, engine.engine_mongodb

# engine = EngineCsv("/home/trannguyenhan/dataset/ign.csv")
# schema = engine.extract_schema()
# print(schema)

# engine = engine.engine_json.EngineJson("/home/trannguyenhan/dataset/alonhadat/house_price_prediction.json")
# schema = engine.extract_schema()

# print(schema)

# engine = engine.engine_mysql.EngineMysql("localhost", "root", "mysql12345", "foodapi", "orders")
# schema = engine.extract_schema()
# print(schema)
# engine.extract_header()
# print(engine.header)


# engine = engine.engine_mssql.EngineMssql("localhost", "sa", "Helloworld123", "test_database", "users")
# schema = engine.extract_schema()
# print(schema)

engine = engine.engine_mongodb.EngineMongodb("localhost", "", "", "X-news", "news")
# engine.extract_header()
# print(engine.header)
schema = engine.extract_schema()
print(schema)