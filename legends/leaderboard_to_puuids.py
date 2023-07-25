import json
import pprint
import ast
from pymongo import MongoClient

with open("mastersplus.txt", 'r', encoding="utf-8") as file:
    client = MongoClient("localhost", 27017)
    db = client["legends"]
    collection = db["puuid"]
    hej = file.read()
    string_list_of_dicts = hej.replace("'", "\"")
    tolist = ast.literal_eval(string_list_of_dicts)
    liste = []

    for i in tolist:
        liste.append(dict(i))
    list_of_puuids = []
    for j in liste[0]["divisions"][0]["standings"]:
        list_of_puuids.append(j["puuid"])
    print(list_of_puuids)
    # collection.insert_one({"rank": "m", "list": list_of_puuids})
