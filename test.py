# this is file test engine

import engine.engine, engine.engine_csv, engine.engine_json, engine.engine_mssql, engine.engine_mysql, engine.engine_xml, engine.engine_mongodb

# engine = engine.engine_csv.EngineCsv("/home/trannguyenhan/dataset/ign.csv")
# engine.dump_data_to_warehouse(
#     ['number_t', 'score_phrase_t', 'title_t', 'url_t', 'platform_t', 'score_t', 'genre_t', 'editors_choice_t', 
#         'release_year_t', 'release_month_t', 'release_day_t', 'col1_t', 'col2_t', 'col3_t'], "proj2")
# print(engine.header)

# engine = engine.engine_json.EngineJson("/home/trannguyenhan/dataset/alonhadat/house_price_prediction.json")
# result = engine.dump_data_to_warehouse(
#     ['type_t', 'bedroom_number_t', 'floor_number_t', 'is_dinning_room_t', 'height_t', 'start_date_t', 'is_terrace_t', 
#         'street_in_front_of_house_t', 'area_t', 'description_t', 'end_date_t', 'law_t', 'is_owner_t', 'width_t', 'direction_t', 
#             'address_t', '_id_t', 'is_kitchen_t', 'is_car_pack_t', 'price_t'], "proj2")
# print(result)
# engine.extract_header()
# print(engine.header)

# print(schema)

# engine = engine.engine_mysql.EngineMysql("localhost", "root", "mysql12345", "foodapi", "orders")
# engine.dump_data_to_warehouse(
#     ['id', 'user_id', 'food_id', 'address', 'time', 'status', 'code'], "proj4")
# schema = engine.extract_schema()
# print(schema)
# engine.extract_header()
# print(engine.header)


# engine = engine.engine_mssql.EngineMssql("localhost", "sa", "Helloworld123", "test_database", "users")
# schema = engine.extract_schema()
# print(schema)

# engine = engine.engine_mongodb.EngineMongodb("localhost", "", "", "datawarehouse", "proj2")
# engine.extract_header()
# print(engine.header)
# schema = engine.extract_schema()
# print(schema)
# engine.save_data({"data": 2, "beta": 2}, "testproject")

engine = engine.engine_xml.EngineXml("/home/trannguyenhan/CodeFolder/tmp/test.xml")
# engine.extract_header()
# print(engine.data_sample)
engine.dump_data_to_warehouse(['rank', 'year', 'gdppc', 'neighbor'], 'proj5')