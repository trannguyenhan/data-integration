import random

import pandas as pd
import pymongo
import recordlinkage
from pandas.api.types import (is_datetime64_dtype, is_numeric_dtype,
                              is_string_dtype)
from pymongo import MongoClient
from recordlinkage.index import Full


def find_duplicate(collection): 
    data = pd.DataFrame(list(collection.find()))
    data.set_index("_id",drop = True, inplace = True)
    print(data.info())
    print(len(data.columns))
    print(data.columns[0])

    print("==============================")
    if len(data.columns) < 1 or collection.count_documents({})<2:
        return []
    # Indexation step
    indexer = recordlinkage.Index()
    if collection.count_documents({}) > 70:
        indexer.block(left_on=data.columns[0])
    else:
        indexer.add(Full())
    candidate_links = indexer.index(data)

    print("Total docs: "+ str(collection.count_documents({})))
    print("Compare amount: "+ str(len(candidate_links)))

    compare_cl = recordlinkage.Compare()
    string_compare_methods = ['jarowinkler','levenshtein', 'damerau_levenshtein', 'qgram', 'cosine']

    for label in data.columns:
        if is_string_dtype(data[label]):
            compare_cl.string(label, label, method=random.choice(string_compare_methods) , threshold=0.85)
        elif is_numeric_dtype(data[label]):
            compare_cl.numeric(label, label)
        elif is_datetime64_dtype(data[label]):
            compare_cl.date(label, label)


    # Comparison step

    features = compare_cl.compute(candidate_links, data)
    upper_bound = (len(data.columns)*3) //4 if len(data.columns) > 2 else len(data.columns)  
    # Classification step
    matches = features[features.sum(axis=1) >= upper_bound]
    print(matches)
    ids_1,ids_2 = map(list,zip(*list(matches.index)))
    return ids_2

