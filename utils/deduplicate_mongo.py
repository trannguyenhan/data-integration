import random

import pandas as pd
import pymongo
import recordlinkage
from pandas.api.types import (is_datetime64_dtype, is_numeric_dtype,
                              is_string_dtype)
from pymongo import MongoClient
from recordlinkage.index import Full

from utils.constants import DataType
from utils.context import Context

dict_convert = {
    DataType.INT : pd.to_numeric, 
    DataType.DATE : pd.to_datetime,
    DataType.FLOAT : pd.to_numeric,
}

def find_duplicate(collection): 
    data = pd.DataFrame(list(collection.find()))
    data.set_index("_id",drop = True, inplace = True)
    schema = Context.project["destination schema"]
    for column in schema.keys():
        if schema[column] in dict_convert:
            data[column] = dict_convert[schema[column]](data[column], errors='coerce')
        else:
            data[column] = data[column].astype("string", errors='ignore')
    data = data.dropna()

    print("==============================")
    print(data.info())

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
    string_compare_methods = [('jaro', 0.75),('jarowinkler',0.75), ('levenshtein',0.65), ('damerau_levenshtein',0.8), ('qgram',0.85),('cosine',0.85), ('smith_waterman',0.85), ('lcs',0.85)]

    for label in data.columns:
        if is_string_dtype(data[label]):
            method, ths = random.choice(string_compare_methods)
            compare_cl.string(label, label, method= method, threshold=ths)
        elif is_numeric_dtype(data[label]):
            compare_cl.numeric(label, label)
        elif is_datetime64_dtype(data[label]):
            compare_cl.date(label, label)

    # Comparison step

    features = compare_cl.compute(candidate_links, data)
    features.to_csv("compare.csv")
    upper_bound = (len(data.columns)*3) //4 if len(data.columns) > 2 else len(data.columns)  
    # Classification step
    matches = features[features.sum(axis=1) >= upper_bound]
    print("Total duplicate: " +str(len(matches)))
    if len(matches) == 0:
        return []
    ids_1,ids_2 = map(list,zip(*list(matches.index)))
    return list(dict.fromkeys(ids_2))

