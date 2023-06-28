import requests
from pymongo import MongoClient
import time

# use https://developer.riotgames.com/apis#tft-match-v1/GET_getMatchIdsByPUUID
# search for the puuid when looking their matches through and find out if they are running same comp or not every game.
# +15 should be enough.

def find_matches(server, player):
    pass

def is_player_onetrick(server, player, matches):
    pass

    # we save the find, having the server, name and see if they are one trick or not
    # then we just check on some aggregate site such as lolchess.com to figure out if how they play.


def main():
    # I connect to db in main and do the requests through find matches.
    client = MongoClient("localhost", 27017)
    database = client["Onetrick"]
    collections = ['master_br1', 'grandmaster_br1', 'challenger_br1', 'master_eun1', 'grandmaster_eun1', 'challenger_eun1',
           'master_euw1', 'grandmaster_euw1', 'challenger_euw1', 'master_jp1', 'grandmaster_jp1', 'challenger_jp1',
           'master_kr', 'grandmaster_kr', 'challenger_kr', 'master_la1', 'grandmaster_la1', 'challenger_la1','master_la2',
           'grandmaster_la2', 'challenger_la2', 'master_na1', 'grandmaster_na1', 'challenger_na1', 'master_oc1',
           'grandmaster_oc1', 'challenger_oc1', 'master_ph2', 'grandmaster_ph2', 'challenger_ph2', 'master_ru',
           'grandmaster_ru', 'challenger_ru', 'master_sg2', 'grandmaster_sg2', 'challenger_sg2', 'master_th2',
           'grandmaster_th2', 'challenger_th2', 'master_tr1', 'grandmaster_tr1', 'challenger_tr1', 'master_tw2',
           'grandmaster_tw2', 'challenger_tw2', 'master_vn2', 'grandmaster_vn2', 'challenger_vn2']
    for collection in collections:
        league_server =  database[collection]
        documents = list(league_server.find())
        # Here I just call find matches and manipulate them inside of find matches and then we run is player onetrick and finish

    print("hej")


if __name__ == '__main__':
    main()
