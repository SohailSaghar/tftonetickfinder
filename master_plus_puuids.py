import requests
from pymongo import MongoClient
import time

# global variables
headers = {
    # api key. needs to be refreshed every 24 hrs.
    'X-Riot-Token': ''
}


# the point of this file will be to save the puuid of master+ players to a db.
def request_summoner_id(server, league) -> list:
    url = f"https://{server}.api.riotgames.com/tft/league/v1/{league}"

    response = requests.request("GET", url, headers=headers)
    response_json = response.json()
    list_of_summoner_ids = []
    for player in response_json["entries"]:
        list_of_summoner_ids.append(player["summonerId"])
    print(list_of_summoner_ids)
    return list_of_summoner_ids


def summoner_id_to_puuid(server, list_of_summoner_ids):
    list_of_puuid = []

    for summoner_id in list_of_summoner_ids:
        # rate limit of 100 requests every 2 minutes(s).
        time.sleep(2)
        url = f"https://{server}.api.riotgames.com/lol/summoner/v4/summoners/{summoner_id}"

        response = requests.request("GET", url, headers=headers)
        response_json = response.json()

        dict_of_relevant_data = {"puuid": response_json["puuid"], "summonerName": response_json["name"]}
        print("appending:" + str(dict_of_relevant_data))
        list_of_puuid.append(dict_of_relevant_data)

    return list_of_puuid


def save_to_db(server, league, list_of_puuid):
    client = MongoClient("localhost", 27017)

    db = client["Onetrick"]
    collection = db[f"{league}_{server}"]
    for puuid in list_of_puuid:
        time.sleep(0.1)
        # add a check for if the player already exists.
        collection.insert_one({'puuid': puuid['puuid'], 'summonerName': puuid["summonerName"]})
        print("successfully inserted " + str(puuid))
    client.close()
    print("success!")
