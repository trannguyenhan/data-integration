import pandas as pd
import pymongo
import recordlinkage
from pymongo import MongoClient

client = MongoClient()

# mongoimport --jsonArray --db test --collection student --file file_test.json

db = client.test
collection = db.student
data = pd.DataFrame(list(collection.find()))
data.set_index("_id",drop = True, inplace = True)
print(data.head(5))

print("==============================")

# Indexation step
indexer = recordlinkage.Index()
indexer.block(left_on="given_name")
candidate_links = indexer.index(data)

# Comparison step
compare_cl = recordlinkage.Compare()

compare_cl.exact("given_name", "given_name", label="given_name")
compare_cl.string("surname", "surname", method="jarowinkler", threshold=0.85, label="surname")
compare_cl.exact("date_of_birth", "date_of_birth", label="date_of_birth")
compare_cl.exact("suburb", "suburb", label="suburb")
compare_cl.exact("state", "state", label="state")
compare_cl.string("address_1", "address_1", threshold=0.85, label="address_1")

features = compare_cl.compute(candidate_links, data)

# Classification step
matches = features[features.sum(axis=1) > 3]
print(matches)
