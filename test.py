# this is file test engine

from my_engine import *
import my_engine

# engine = engine_csv.EngineCsv("/home/trannguyenhan/dataset/ign.csv")
# engine.dump_data_to_warehouse(
#     {'number': 'number_t', 'score_phrase': 'score_phrase_t', 'title': 'title_t', 'url': 'url_t'}, "proj2")
# print(engine.get_sample_data())

# engine = engine_json.EngineJson("/home/trannguyenhan/dataset/alonhadat/house_price_prediction.json")
# result = engine.dump_data_to_warehouse(
#     {'type': 'type_t', 'bedroom_number': 'bedroom_number_t', 'floor_number': 'floor_number_t', 'is_dinning_room': 'is_dinning_room_t'}, "proj2")
# print(result)
# engine.extract_header()
# print(engine.header)
# print(len(engine.get_sample_data()))

# print(schema)

# engine = engine_mysql.EngineMysql("localhost", "root", "mysql12345", "foodapi", "orders")
# engine.dump_data_to_warehouse(
#     {'id': 'sid', 'user_id': 'userId', 'food_id': 'foodId'}, "proj4")
# schema = engine.extract_schema()
# print(schema)
# engine.extract_header()
# print(engine.header)
# print(engine.get_sample_data())


# engine = engine.engine_mssql.EngineMssql("localhost", "sa", "Helloworld123", "test_database", "users")
# schema = engine.extract_schema()
# print(schema)

# engine = engine.engine_mongodb.EngineMongodb("localhost", "", "", "datawarehouse", "proj2")
# engine.extract_header()
# print(engine.header)
# schema = engine.extract_schema()
# print(schema)
# engine.save_data({"data": 2, "beta": 2}, "testproject")

# engine = engine_xml.EngineXml("/home/trannguyenhan/CodeFolder/tmp/test.xml")
# engine.extract_header()
# print(engine.data_sample)
# engine.dump_data_to_warehouse({'rank': 'RANK', 'year': 'YEAR'}, 'proj5')
# print(engine.get_sample_data())

# SERVER=localhost;DATABASE=testdb;UID=sa;PWD=1234
# engine = EngineMssql("localhost", "sa", "1234", "testdb", "test")

# engine.extract_header()

my_engine.engine_mongodb.EngineMongodb.to_xml("proj5", ["RANK", "YEAR"])