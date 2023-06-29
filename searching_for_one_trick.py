import requests
from pymongo import MongoClient
import time

# global variables
headers = {
    # api key. needs to be refreshed every 24 hrs.
    'X-Riot-Token': 'RGAPI-b31b6922-20e9-49a6-a6bd-1fde72d68948'
}


# use https://developer.riotgames.com/apis#tft-match-v1/GET_getMatchIdsByPUUID
# search for the puuid when looking their matches through and find out if they are running same comp or not every game.
# 70% of games and more than 3 units are the requirements.

# we save the find, having the server, name and see if they are one trick or not
# then we just check on some aggregate site such as lolchess.com to figure out if how they play.

def find_matches(player, route):
    time.sleep(2)
    matches = []

    url = f"https://{route}.api.riotgames.com/tft/match/v1/matches/by-puuid/{player}/ids"

    response = requests.request("GET", url, headers=headers)
    for match in response.json():
        matches.append(match)
    print(f"matches found for {player}")
    return matches


def player_unit_frequency(player, route, matches):
    units_frequency = {}
    for match in matches:
        time.sleep(2)
        url = f"https://{route}.api.riotgames.com/tft/match/v1/matches/{match}"

        response = requests.request("GET", url, headers=headers)

        # here we find the user which is the player we are looking at.
        for user in range(8):
            if response.json()["info"]["participants"][user]["puuid"] == player:
                for unit in response.json()["info"]["participants"][user]["units"]:
                    if unit["character_id"] in units_frequency:
                        units_frequency[unit["character_id"]] += 1
                    else:
                        units_frequency[unit["character_id"]] = 1
    print(f"item frequency for the player {player} has been calculated")

    return units_frequency


def is_player_onetrick(unit_frequency, num_of_matches):
    """
    The general idea here is that we use the num_of_matches to find a certain percentage which some units
    need to surpass. E.g. let's say that the percentage was 75% then the unit frequency would need to be above this for
    more than 4 units then it would return true otherwise false.
    """
    # constants
    units = unit_frequency.keys()
    sufficient_num_of_units_count = 0
    sufficient_units = 4
    percentage_games = 0.70
    is_onetrick = False

    for unit in units:
        if unit_frequency[unit] / num_of_matches > percentage_games:
            sufficient_num_of_units_count += 1

    if sufficient_num_of_units_count >= sufficient_units:
        is_onetrick = True
    print(f"is onetrick? {is_onetrick}")
    return is_onetrick


def routing(server):
    routes = {"br1": "americas", "eun1": "europe", "euw1": "europe", "jp1": "asia", "kr": "asia",
              "la1": "america", "la2": "america", "na1": "america", "oc1": "sea", "ph2": "sea",
              "ru": "europe", "sg2": "sea", "th2": "sea", "tr1": "europe", "tw2": "sea", "vn2": "sea"}
    return routes[server]


def main():
    # I connect to db in main and do the requests through find matches.
    client = MongoClient("localhost", 27017)
    db = client["Onetrick"]
    collections = ['master_br1', 'grandmaster_br1', 'challenger_br1', 'master_eun1', 'grandmaster_eun1',
                   'challenger_eun1',
                   'master_euw1', 'grandmaster_euw1', 'challenger_euw1', 'master_jp1', 'grandmaster_jp1',
                   'challenger_jp1',
                   'master_kr', 'grandmaster_kr', 'challenger_kr', 'master_la1', 'grandmaster_la1', 'challenger_la1',
                   'master_la2',
                   'grandmaster_la2', 'challenger_la2', 'master_na1', 'grandmaster_na1', 'challenger_na1', 'master_oc1',
                   'grandmaster_oc1', 'challenger_oc1', 'master_ph2', 'grandmaster_ph2', 'challenger_ph2', 'master_ru',
                   'grandmaster_ru', 'challenger_ru', 'master_sg2', 'grandmaster_sg2', 'challenger_sg2', 'master_th2',
                   'grandmaster_th2', 'challenger_th2', 'master_tr1', 'grandmaster_tr1', 'challenger_tr1', 'master_tw2',
                   'grandmaster_tw2', 'challenger_tw2', 'master_vn2', 'grandmaster_vn2', 'challenger_vn2']

    for collection in collections:

        league_server = db[collection]
        documents = list(league_server.find())
        server = collection.split("_")[1]  # splits on _ and selects server
        route = routing(server)

        for entry in documents:

            player = entry["puuid"]
            matches = find_matches(player, route)
            unit_frequency = player_unit_frequency(player, route, matches)
            is_onetrick = is_player_onetrick(unit_frequency, len(matches))
            if is_onetrick:
                access_to_onetricks = db["certified_onetrick"]
                access_to_onetricks.insert_one(
                    {'puuid': player, 'summonerName': entry["summonerName"], 'server': server})
# Note that rate limits are enforced per routing value (e.g., na1, euw1, americas).
# meaning we can still upgrade this

if __name__ == '__main__':
    main()
