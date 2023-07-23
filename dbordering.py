from pymongo import MongoClient
from operator import itemgetter


def order_in_descending():
    client = MongoClient("localhost", 27017)
    db = client["Onetrick"]
    collections = db["certified_onetrick"]
    find_all = list(collections.find())

    sorted_in_descending = sorted(find_all, key=itemgetter("avg. placement"))
    order_by_server = sorted(sorted_in_descending, key=itemgetter("server"))

    for player in order_by_server:
        print(player)


if __name__ == '__main__':
    order_in_descending()
