import requests
from pymongo import MongoClient
import time


# the point of this file will be to save the puuid of master+ players to a db.
def request_summoner_id(server, league):
    url = f"https://{server}.api.riotgames.com/tft/league/v1/{league}"

    headers = {
        # api key. needs to be refreshed every 24 hrs.
        'X-Riot-Token': 'RGAPI-389d3c06-414d-4478-887e-a61585be2656'
    }

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

        headers = {
            'X-Riot-Token': 'RGAPI-389d3c06-414d-4478-887e-a61585be2656'
        }

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
        collection.insert_one({'puuid': puuid['puuid'], 'summonerName': puuid["summonerName"]})
        print("successfully inserted " + str(puuid))
    client.close()
    print("success!")


def main():
    servers = ["br1", "eun1", "euw1", "jp1", "kr",
               "la1", "la2", "na1", "oc1", "ph2",
               "ru", "sg2", "th2", "tr1", "tw2", "vn2"
               ]
    leagues = ["master", "grandmaster", "challenger"]

    for server in servers:
        for league in leagues:
            summoner_ids = request_summoner_id(server, league)
            puuids = summoner_id_to_puuid(server, summoner_ids)
            save_to_db(server, league, puuids)


if __name__ == '__main__':
    main()
